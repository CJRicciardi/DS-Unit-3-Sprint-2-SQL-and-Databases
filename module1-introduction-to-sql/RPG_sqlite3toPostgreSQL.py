# RPG_sqlite3toPostgreSQL.py

import sqlite3 as lite
import os
import psycopg2 as psy2
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

## Get the list of tables
# connect to rpg_db.sqlite3
lite_connection = lite.connect("rpg_db.sqlite3")

# create cursor
lite_cursor = lite_connection.cursor()


# create query to return list of tables
table_list_query = """
                   SELECT name FROM sqlite_master
                   WHERE type='table'
                   ORDER BY name
                   """

# execute table_list_query
table_tuple = lite_cursor.execute(table_list_query).fetchall()
# print(table_tuple)

# convert table_tuple to table_list
table_list = []
for i in range(0, len(table_tuple)):
    table_list.append(table_tuple[i][0])
# print(table_list)

# pipeline for loop
for table in table_list:

    # set up pipeline for a single table
    # table_string = 'armory_item'

    # create query to load table
    table_query = f'''
                   SELECT *
                   FROM {table}
                   '''

    # name table df after table
    df = pd.read_sql_query(table_query, lite_connection)

    #assign URL
    URL = os.getenv('RPG_pipeline_URL', default='oops')

    #create SQL engine
    engine = create_engine(URL)

    #convert table
    df.to_sql(table, engine)
    engine.connect().close()
    # print(df)

engine.dispose()

# # (Background on this error at: http://sqlalche.me/e/e3q8)
