# demo_data.py

import sqlite3 as lite
import os
import pandas as  pd

# construct path to demo_data.sqlite3
demo_connection = lite.connect("demo_data.sqlite3")
#print("Demo Connection:", demo_connection)

# create cursor for sqlite3
demo_cursor = demo_connection.cursor()
#print("Demo Cursor:", demo_cursor)

# create demo table creation query
create_demo_query = """
    CREATE TABLE IF NOT EXISTS demo (
        s varchar(1),
        x int,
        y int
        );
    """

# execute create_demo_query
demo_cursor.execute(create_demo_query)

# create insert data statement query
demo_data_query = """
    INSERT INTO demo
    VALUES ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
    ON CONFLICT DO NOTHING
    """

# execute demo_data_query
demo_cursor.execute(demo_data_query)

#commit above queries
demo_connection.commit()

# count rows query, execute & print answer
row_count = """
SELECT COUNT(*)
FROM demo
"""
result = demo_cursor.execute(row_count).fetchall()
print(f"\nDemo DB has {result[0][0]} rows.")

# count where x & y are greater than 5 - query, execute and answer
xy_count = """
SELECT COUNT(*)
FROM demo
WHERE x > 5 AND y > 5
"""
result2 = demo_cursor.execute(xy_count).fetchall()
print(f"\nDemo DB has {result2[0][0]} instances where both x and y are greater than five.")

# count distinct y - query, execute, and answer
distinct_y = """
SELECT COUNT(DISTINCT y)
FROM demo;
"""
result3 = demo_cursor.execute(distinct_y).fetchall()
print(f"\nDemo DB has {result3[0][0]} unique y values.")

demo_connection.close()