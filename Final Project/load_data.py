import sqlite3
import pandas as pd

CSV_FILE = "Data centric assignment data.csv"
DB_FILE = "spending.db"

# 1. Read the CSV (utf-8-sig removes the invisible Excel character)
df = pd.read_csv(CSV_FILE, encoding="utf-8-sig")

# 2. Give the columns simple names (same order as my CSV)
df.columns = ["date", "price", "location", "need_want", "payment",
              "description", "category", "online_or_in_person"]

# 3. Clean the text columns: remove extra spaces and make the capital letters consistent
text_columns = ["location", "need_want", "payment", "description", "category", "online_or_in_person"]
for column in text_columns:
    df[column] = df[column].str.strip()

df["need_want"] = df["need_want"].str.lower()
df["payment"] = df["payment"].str.lower()
df["online_or_in_person"] = df["online_or_in_person"].str.lower()
df["category"] = df["category"].str.title()

# 4. Check the types: dates and prices
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y").dt.strftime("%Y-%m-%d")
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# 5. Handle missing values: remove any row with a missing date or price
missing = df[df["date"].isna() | df["price"].isna()]
if len(missing) > 0:
    print("Removing rows with a missing date or price:")
    print(missing)
    df = df.drop(missing.index)

# 6. Flag out of range prices (kept in the data, just shown as a warning)
too_big = df[df["price"] > 150]
too_small = df[df["price"] <= 0]
print("Prices over 150 euro (please check these are correct):")
print(too_big[["date", "price", "description"]])
print("Prices of 0 or less:", len(too_small))

# 7. Put the data into a SQLite database
conn = sqlite3.connect(DB_FILE)
conn.execute("DROP TABLE IF EXISTS purchases")
conn.execute("""
    CREATE TABLE purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        price REAL,
        location TEXT,
        need_want TEXT,
        payment TEXT,
        description TEXT,
        category TEXT,
        online_or_in_person TEXT
    )
""")
df.to_sql("purchases", conn, if_exists="append", index=False)
conn.commit()

# 8. Check it worked
count = conn.execute("SELECT COUNT(*) FROM purchases").fetchone()[0]
print("Rows in the database:", count)
print(conn.execute("SELECT * FROM purchases LIMIT 3").fetchall())
print(conn.execute("SELECT DISTINCT category FROM purchases").fetchall())
conn.close()
