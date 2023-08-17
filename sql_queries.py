# DROP TABLES

songplay_table_drop = "Drop table if exists songplays"
user_table_drop = "Drop table if exists users"
song_table_drop = "Drop table if exists songs"
artist_table_drop = "Drop table if exists artists"
time_table_drop = "Drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplays \
                         (songplay_id SERIAL PRIMARY KEY,
                         start_time timestamp NOT NULL, 
                         user_id int NOT NULL, 
                         level varchar,
                        song_id varchar, 
                        artist_id varchar, 
                        session_id int, 
                        location varchar, 
                        user_agent varchar );""")

user_table_create = ("""create table if not exists users \
                     (user_id int NOT NULL, 
                     first_name varchar, 
                     last_name varchar, 
                     gender varchar, 
                     level varchar, 
                     PRIMARY KEY (user_id));""")

song_table_create = ("""create table if not exists songs \
                     (song_id varchar NOT NULL, 
                     title varchar NOT NULL, 
                     artist_id varchar, 
                     year int, duration float, 
                     PRIMARY KEY (song_id));
""")

artist_table_create = ("""create table if not exists artists \
                       (artist_id varchar NOT NULL, 
                       name varchar NOT NULL, 
                       location varchar, 
                       latitude float, 
                       longitude float, 
                       PRIMARY KEY (artist_id));
""")

time_table_create = ("""create table if not exists time\
                     (start_time timestamp NOT NULL, 
                     hours int, 
                     day int, 
                     week int, 
                     month int, 
                     year int, 
                     weekday int, 
                     PRIMARY KEY (start_time));
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays \
                         (start_time, 
                         user_id, 
                         level, 
                         song_id, 
                         artist_id, 
                         session_id, 
                         location, 
                         user_agent)
                        VALUES (%s, %s, %s, %s,%s, %s, %s, %s)
                        ON CONFLICT (songplay_id) DO NOTHING;""")

user_table_insert = ("""INSERT INTO users 
                     (user_id, 
                     first_name, 
                     last_name, 
                     gender, 
                     level)
                     VALUES (%s, %s, %s, %s, %s)
                     ON CONFLICT (user_id) 
                     DO UPDATE SET level = EXCLUDED.level;""")

song_table_insert = ("""INSERT INTO songs 
                     (song_id, 
                     title, \
                     artist_id, 
                     year, duration)
                     VALUES (%s, %s, %s, %s, %s)
                     ON CONFLICT (song_id) 
                     DO UPDATE SET 
                     title = EXCLUDED.title  || ';' || songs.title ;""")

artist_table_insert = ("""INSERT INTO artists 
                       (artist_id, 
                       name, 
                       location, 
                       latitude, 
                       longitude)
                       VALUES (%s, %s, %s, %s, %s)
                       ON CONFLICT (artist_id) 
                       DO UPDATE SET 
                       name = EXCLUDED.name || ';' || artists.name ;""")

time_table_insert = ("""INSERT INTO TIME 
                     (start_time, 
                     hours, 
                     day, \
                     week,
                     month, 
                     year, 
                     weekday)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)
                     ON CONFLICT (start_time) DO NOTHING;""")


# FIND SONGS

song_select = ("""select songs.song_id, artists.artist_id \
                FROM songs JOIN artists 
                on songs.artist_id = artists.artist_id \
                WHERE songs.title = %s
                AND artists.name = %s
                AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, 
                        user_table_create, 
                        song_table_create, 
                        artist_table_create, 
                        time_table_create]

drop_table_queries = [songplay_table_drop, 
                      user_table_drop, 
                      song_table_drop, 
                      artist_table_drop, 
                      time_table_drop]
