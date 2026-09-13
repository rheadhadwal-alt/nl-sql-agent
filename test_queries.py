import sqlite3
import pandas as pd

conn = sqlite3.connect("Sample - Superstore.db")

# Query 1: row count
print(pd.read_sql("SELECT COUNT(*) AS row_count FROM orders;", conn))
git
# Query 2: total sales by region
print(pd.read_sql("""
    SELECT region, ROUND(SUM(sales), 2) AS total_sales
    FROM orders
    GROUP BY region
    ORDER BY total_sales DESC;
""", conn))

# Query 3: sanity-check dates
print(pd.read_sql("SELECT MIN(order_date), MAX(order_date) FROM orders;", conn))

conn.close()