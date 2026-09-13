import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")  # Superstore CSVs often need latin1 encoding

print(df.shape)
print(df.dtypes)
print(df.head())
print(df.isnull().sum())

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)
print(df.columns.tolist())

df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

df.to_csv("Sample - Superstore.csv", index=False)