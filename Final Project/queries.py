import sqlite3
import pandas as pd

conn = sqlite3.connect("spending.db")


def show(title, sql):
    """Run a SQL query and print the result as a table."""
    print("\n" + title)
    print(pd.read_sql(sql, conn).to_string(index=False))


# 1. How much have I spent in total? 
show("1. Overall totals", """
    SELECT COUNT(*) AS purchases,
           ROUND(SUM(price), 2) AS total_spent,
           ROUND(AVG(price), 2) AS average_purchase
    FROM purchases
""")

# 2. Where does my money go? 
show("2. Spending by category", """
    SELECT category,
           COUNT(*) AS purchases,
           ROUND(SUM(price), 2) AS total_spent
    FROM purchases
    GROUP BY category
    ORDER BY total_spent DESC
""")

# 3. My question: online or in person?
show("3. Online vs in person", """
    SELECT online_or_in_person,
           COUNT(*) AS purchases,
           ROUND(SUM(price), 2) AS total_spent,
           ROUND(AVG(price), 2) AS average_purchase
    FROM purchases
    GROUP BY online_or_in_person
""")

# 4. My question: weekends or weekdays?
# strftime('%w', date) gives the day number: 0 = Sunday ... 6 = Saturday
show("4. Weekends vs weekdays", """
    SELECT CASE WHEN strftime('%w', date) IN ('0', '6') THEN 'Weekend' ELSE 'Weekday' END AS day_type,
           COUNT(*) AS purchases,
           ROUND(SUM(price), 2) AS total_spent
    FROM purchases
    GROUP BY day_type
""")

# 5. Which purchases cost more than 50 euro? 
show("5. Purchases over 50 euro", """
    SELECT date, price, location, description
    FROM purchases
    WHERE price > 50
    ORDER BY price DESC
""")

conn.close()
