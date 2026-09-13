import sqlite3
import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", parse_dates=["order_date", "ship_date"])

conn = sqlite3.connect("Sample - Superstore.db")
df.to_sql("orders", conn, if_exists="replace", index=False)
conn.close()

print("Loaded into SQLite as table 'orders'")