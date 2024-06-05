import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect('./chinook_db_files/chinook_db/chinook.db')
cursor = conn.cursor()

# SQL query to find the customer with the highest total spending
query = """
SELECT
    'Customer ' || C.CustomerId AS CustomerName,
    SUM(IL.UnitPrice * IL.Quantity) AS TotalSpent
FROM
    Customer AS C
JOIN
    Invoice AS I ON C.CustomerId = I.CustomerId
JOIN
    InvoiceLine AS IL ON I.InvoiceId = IL.InvoiceId
GROUP BY
    C.CustomerId
ORDER BY
    TotalSpent DESC
LIMIT 1;
"""

try:
  cursor.execute(query)
  result = cursor.fetchone()
  if result:
    customer_name, total_spent = result
    print(f'The best customer is {customer_name} with a total spending of ${total_spent:.2f}')
  else:
    print("No results found.")
except Exception as e:
  print("Error", str(e))