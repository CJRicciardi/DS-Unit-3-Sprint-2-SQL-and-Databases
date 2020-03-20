# northwind.py

import sqlite3 as lite
import os
import pandas as pd

# construct path to northwind_small.sqlite3
connection = lite.connect("northwind_small.sqlite3")
#print("Connection:", connection)

# create cursor instance for connection
cursor = connection.cursor()
#print("Cursor:", cursor)

# query, execution and result for ten most expensive products
expensive_query = """
    SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
    """
result = cursor.execute(expensive_query).fetchall()
pretty_result = pd.DataFrame(result, columns=["Item", "Price"])
print(f"\nThe ten most expensive items are:", pretty_result)

# query, execute, and result for largest category
category_count = """
    SELECT CategoryId, COUNT(CategoryId) AS "Count"
    FROM Product
    GROUP BY CategoryId
    LIMIT 1;
    """
result2 = cursor.execute(category_count).fetchall()
print(f"\nCategory {result2[0][0]} has the most items, with {result2[0][1]} items.")

connection.close()