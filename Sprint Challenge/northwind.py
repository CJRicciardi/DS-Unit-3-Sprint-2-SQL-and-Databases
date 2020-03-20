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

# query, execution and answer for average age at hire
hire_age = """
    SELECT AVG(HireDate - BirthDate)
    FROM Employee;
    """
result3 = cursor.execute(hire_age).fetchall()
print(f"\nThe average age of a newly hired employee at Northwind is {result3[0][0]:.2f}.")

# query, execute and answer for what are the ten most expensive items and their suppliers
expensive_supplier = """
    SELECT p.ProductName, p.UnitPrice, s.CompanyName
    FROM Product as p 
    LEFT JOIN Supplier as s 
        	ON p.SupplierID = s.ID
    ORDER BY UnitPrice DESC
    LIMIT 10;
    """
result4 = cursor.execute(expensive_supplier).fetchall()
pretty_result4 = pd.DataFrame(result4, columns=["Item", "Price", "Supplier"])
print(f"\nThe ten most expensive items and their supplier are:\n", pretty_result4)

# query, execute, and answer for largest category
category_count = """
    SELECT CategoryId, COUNT(CategoryId) AS "Count"
    FROM Product
    GROUP BY CategoryId
    LIMIT 1;
    """
result2 = cursor.execute(category_count).fetchall()
print(f"\nCategory {result2[0][0]} has the most items, with {result2[0][1]} items.")

connection.close()