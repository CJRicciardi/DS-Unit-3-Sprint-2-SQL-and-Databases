import psycopg2 as psy2 
import os
from dotenv import load_dotenv
import json
from psycopg2.extras import execute_values

load_dotenv()

dbname = os.getenv('dbname', default='oops')
user = os.getenv('user', default='oops')
password = os.getenv('password', default='oops')
host = os.getenv('host', default='oops')

connection = psy2.connect(dbname=dbname, user=user, password=password, host=host)
print('Connection:', connection)

cursor = connection.cursor()
print('Cursor:', cursor)

cursor.execute("SELECT * from test_table;")

result = cursor.fetchone()
print("Result:", result)

# add multiple rows
my_dict = {'a': 1, 'b': ['dog', 'cat', 42], 'c': 'true'}

insertion_query = 'INSERT INTO test_table (name, data) VALUES %s'
execute_values(cursor, insertion_query, [
    ('A row', 'null'),
    ('Another row, with JSON', json.dumps(my_dict)),
    ('Third row', '3')
])

cursor.execute("SELECT * FROM test_table;")
result = cursor.fetchall()
print('Result:', result)

# save transaction
connection.commit()