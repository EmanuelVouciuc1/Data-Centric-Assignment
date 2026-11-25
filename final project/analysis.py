# analysis.py - my pandas toolbox.
# Each function below answers one question about my spending.
# main.py and charts.py import this file and call these functions.

import sqlite3
import pandas as pd


def load_data():
    """Read every purchase out of the database into a pandas table (a DataFrame)."""
    # Open a connection to the database file made by load_data.py
    conn = sqlite3.connect("spending.db")
    # Run one SQL line to grab the whole purchases table.
    # parse_dates turns the date text into real dates so pandas can do date maths.
    df = pd.read_sql("SELECT * FROM purchases", conn, parse_dates=["date"])
    # Close the connection, I have everything I need in df now
    conn.close()
    # Add a column with the name of the day (Monday, Tuesday...) worked out from the date
    df["weekday"] = df["date"].dt.day_name()
    return df


def daily_totals(df):
    """Total spent on each day, including the days I spent nothing (those show as 0)."""
    # Group all purchases by date and add up the prices for each date.
    # Days where I bought nothing are missing from this at the moment.
    daily = df.groupby("date")["price"].sum()
    # Make a list of EVERY day from my first purchase to my last
    all_days = pd.date_range(daily.index.min(), daily.index.max())
    # Line the totals up against every day, filling the missing days with 0
    return daily.reindex(all_days, fill_value=0)


def total_by(df, column):
    """Count, total and average spending, grouped by any column (category, payment...)."""
    # Group by the column I pass in, then work out three things from the price:
    # how many purchases, the total, and the average
    result = df.groupby(column)["price"].agg(purchases="count", total="sum", average="mean")
    # Biggest total first, and round the money to 2 decimal places
    return result.sort_values("total", ascending=False).round(2)


def weekend_vs_weekday(df):
    """Average spent PER DAY on weekends compared with weekdays."""
    # Use the daily totals so the days I spent nothing are counted too (fairer average)
    daily = daily_totals(df)
    # dayofweek is 0 for Monday up to 6 for Sunday, so 5 and 6 are the weekend.
    # This makes a label ("Weekend" or "Weekday") for every single day.
    day_type = ["Weekend" if day.dayofweek >= 5 else "Weekday" for day in daily.index]
    # Group the days by their label and take the average of each group
    return daily.groupby(day_type).mean().round(2)


def spending_by_weekday(df):
    """Average spent on each day of the week (Monday to Sunday)."""
    # Again use the daily totals so empty days count as 0
    daily = daily_totals(df)
    # Group the days by their name and average each group
    average = daily.groupby(daily.index.day_name()).mean()
    # Groups come out in alphabetical order, so put them back in week order
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return average.reindex(order).round(2)


def biggest_purchases(df, n=5):
    """The n most expensive purchases (5 unless I ask for a different number)."""
    # nlargest picks the n rows with the highest price.
    # Then I keep just the 4 columns I want to look at.
    return df.nlargest(n, "price")[["date", "price", "location", "description"]]


def need_want_by_category(df):
    """For each category, how much I spent on needs and how much on wants."""
    # A pivot table: one row per category, one column for need and one for want,
    # with the total price in each box. A box with no purchases becomes 0.
    table = df.pivot_table(index="category", columns="need_want", values="price",
                           aggfunc="sum", fill_value=0)
    return table.round(2)


def days_with_no_purchases(df):
    """The dates where I spent nothing."""
    daily = daily_totals(df)
    # Keep only the days whose total is 0 and return their dates
    return daily[daily == 0].index


def price_summary(df):
    """Quick stats on the price column: count, average, median (50%), smallest, biggest."""
    return df["price"].describe().round(2)


# This part only runs when I run analysis.py directly (not when another file imports it).
# It prints every answer so I can check them.
if __name__ == "__main__":
    df = load_data()
    print("Spending per day:\n", daily_totals(df))
    print("\nWeekend vs weekday:\n", weekend_vs_weekday(df))
    print("\nBy weekday:\n", spending_by_weekday(df))
    print("\nBy category:\n", total_by(df, "category"))
    print("\nBiggest purchases:\n", biggest_purchases(df))
    print("\nNeed vs want by category:\n", need_want_by_category(df))
    print("\nDays with no purchases:\n", days_with_no_purchases(df))
    print("\nPrice summary:\n", price_summary(df))
