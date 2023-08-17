import os
import glob
import json
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    
    """ 
    - This function takes 2 arguments , the cursor and each file that was found by the process_data function. 
    - The function will first read the file and use json.load into the data frame call df,
    - The song_data and artist_data data frames will only take the necessary columns from the df data frame,
    - The cursor execute the song_table_insert/artist_data query, and pass the data into the tables
    """ 
    #open song file
    with open(filepath,'r') as file:
        df = json.load(file)


    # insert song record
        song_data = [df['song_id'],
                    df['title'],
                    df['artist_id'],
                    df['year'],
                    df['duration']]
                    
    
        cur.execute(song_table_insert, song_data)
    
    # insert artist record
        artist_data = [df['artist_id'],
                    df['artist_name'],
                    df['artist_location'],
                    df['artist_latitude'],
                    df['artist_longitude']]
        
        cur.execute(artist_table_insert, artist_data)

def process_log_file(cur, filepath):
    
    """
    - This function takes 2 arguments, the cursor and each of the log file that was found by the process_data function. 
    - Each files will be read and store into a list, the list log_list will be convert into data frame call log_df
    - Filter the rows only if page column equarl to nextsong.
    """
    # open log file
    with open(filepath, 'r') as file:
        log_list = []
        for line in file:
            log_data = json.loads(line)
            log_list.append(log_data)
       
    log_df = pd.DataFrame(log_list)
    # filter by NextSong action
    log_df = log_df[log_df['page'] == 'NextSong']

    # convert timestamp column to datetime
    log_df['ts'] = pd.to_datetime(log_df['ts'], unit='ms')
    
    t = pd.to_datetime(log_df['ts'], unit='ms')
    
    # insert time data records
    time_data = [
        t,
        t.dt.hour,
        t.dt.day,
        t.dt.weekofyear,
        t.dt.month,
        t.dt.year,
        t.dt.weekday
    ]
    column_labels = ['timestamp', 'hour', 'day', 'week_of_year', 'month', 'year', 'weekday']
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    """
    - After convet the ts column datetime format, time_df data frame was created.
    - Cursor execute the time_table_insert query and pass the data into the table.
    - Same as user_df, it only takes the necessary columns from the log_df data frame,
    - Cursor execute the user_table_insert query and pass the data into the table.
    """
    for i, row in time_df.iterrows(): 
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = pd.DataFrame({'user_id': log_df['userId'].astype(int), 'first_name': log_df['firstName'],
                            'last_name': log_df['lastName'],'gender': log_df['gender'],
                             'level': log_df['level']})

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    """
    - In the for loop, use index and row loop through each row in the log_df
    - Cursor first execute the song_select query to loop for matching values from songs and artists table, 
    - The values will be fetched back and save into the song_id and artist_id variables, or it save as none if not exists.
    - songplay_data extract the necessary data from log_df data frame, with log_df index as primary key
    - Cursor execute song_table_insert query to pass the values into songplay table
    """
    # insert songplay records
    for index, row in log_df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record

        songplay_data = [row.ts, int(row.userId), row.level, songid, artistid, row.sessionId, row.location, row.userAgent]
        cur.execute(songplay_table_insert, songplay_data)

def process_data(cur, conn, filepath, func):
    
    """
    - This function takes 4 arguments, the curor, the connection info, the key words of target files and the passing function,
    - Before reading each file, the total files that will be read will display
    - Each file will be passed into the process_song_file or process_log_file function,for extract info for the songplay table. 
    
    """
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    
    conn = psycopg2.connect("host=localhost dbname=sparkifydb user=lyttonliang password=1124")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()