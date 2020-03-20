# pg_titanic.py

import os
from dotenv import load_dotenv
import psycopg2 as psy2
from psycopg2.extras import execute_values
import pandas as pd

load_dotenv()  # look at the env file for env functions

# access hiddden db credentials
name = os.getenv("titanic_name", default="oops")
user = os.getenv("titanic_user", default="oops")
password = os.getenv("titanic_password", default="oops")
host = os.getenv("titanic_host", default="oops")

# connect to server
connection = psy2.connect(dbname=name, user=user, password=password, host=host)
print("CONNECTION:", connection)

# create cursor
cursor = connection.cursor()
print("CURSOR:", cursor)

# create the table (query)
create_table = """
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived int,
    pclass int,
    name varchar,
    sex varchar,
    age int,
    siblings_spouses_aboard int,
    parents_children_aboard int,
    fare float8
);
"""

# execute query
cursor.execute(create_table)

# view SQL db
cursor.execute("SELECT * FROM passengers")
result = cursor.fetchall()
print("PASSENGERS:", result)

#
if len(result) == 0:
    # insert records

    csv_filepath = os.path.join(os.path.dirname(__file__), "titanic.csv")
    print("FILE EXISTS?", os.path.isfile(csv_filepath))
    df = pd.read_csv(csv_filepath)
    print(df.head())

    rows = list(df.itertuples(index=False, name=None))

    insertion_query = "INSERT INTO passengers (survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children_aboard, fare) VALUES %s"
    execute_values(cursor, insertion_query, rows)

connection.commit()
