import psycopg2 as psy2 
import os
from dotenv import load_dotenv

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
print("RESULT:", result)

