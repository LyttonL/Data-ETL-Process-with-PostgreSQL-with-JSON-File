# Data Modeling with Postgres


## Table of Contents

- [Introduction](#intro)
- [Instruction](#Instruction)



<a id='intro'></a>
## Introduction

### In this project, I worked with over 100 JSON files collected from a startup called Sparkify.  The goal was to create a Postgres database named Sparkifydb and perform an Extract, Transform, Load (ETL) process. The database consists of five tables: users, songs, time, artists, and songplays.

### By utilizing these five tables, Sparkify can conduct future analysis and enhance the development of their music streaming application. The collected JSON files provided valuable data that was processed and stored in the appropriate tables, enabling Sparkify to gain insights and improve their service in the future.



<a id='Instruction'></a>
## Instruction

### I perform this entire project on my local machine. This file folder should have already include all the nessecery files that will be used to perform the ETL  processes. 

### The files are:
> - etl.ipynb
> - test.ipynb
> - etl.py
> - create_tables.py
> - sql_queries.py
> - README.ipynb
> - data (folder)



### Please change the **connection information** before running the scripts.


#### Here is a step-by-step explanation of how to run all the scripts.

### If you would like to perform the processes in jupyter notebook:


>1. Open the _etl.ipynb_ file in jupyter notebook,

>2. Open the _create_tables.py_ and _sql_queries.py_ on your python environment, 

>3. Change the **connection information** in _etl.ipynb_ and _create_tables.py_,

>4. Run _create_tables.py_, to drop and create new tables, 

>5. Run the whole _etl.ipynb_ notebook,

>6. After step 4, the etl notebook is ran, open _test.ipynb_, run the whole notebook,

>7. Songplays, time, and users tables should display 5 records. Songs and artists tables should only have 1 record. 



### If you would like to perform the processes in your Python environment:


>1. Open the _etl.py_, _create_tables.py_ and _sql_queries.py_ files on your python environment, 

>2. Change the **connection information** in _etl.ipynb_ and _create_tables.py_,

>3. Run _create_tables.py_, to drop and create new tables,

>4. Run _etl.py_, files processed message should prompt with no issue,
 
>5. Log in to your local Postgres application, the database should be created and tables exist,

>6. Or you can open _test.ipynb_ and run the whole notebook, **all 5 tables should have more than 5 records**, but will only display 5 here.  

### If you need to run the notebook multiple times, always restart the Kernel of all the notebooks and run the _create_tables.py_ to reset all the tables. 



```python

```
