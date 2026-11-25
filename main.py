# main.py - the menu for my spending tracker.
# It loads my data from the database once, then keeps showing a menu
# until I choose 0 to quit.

import analysis   # my own file, analysis.py, with the pandas functions

# Read the purchases table from the database into a pandas table (a DataFrame).
# I call it df and every menu option below uses it.
df = analysis.load_data()


def show(table):
    """Print a table of purchases, or a message if there are none."""
    if table.empty:
        print("Nothing found.")
    else:
        # Only show the 4 columns I care about, without the row numbers
        print(table[["date", "price", "location", "description"]].to_string(index=False))


# This loop repeats forever until I type 0 (the break at the bottom stops it)
while True:
    print("\n===== SPENDING TRACKER =====")
    print("1. Overview")
    print("2. Spending breakdowns")
    print("3. Weekends vs weekdays")
    print("4. Purchases over a price")
    print("5. Purchases in one category")
    print("0. Quit")
    # input() waits for me to type, strip() removes any accidental spaces
    choice = input("Choose an option: ").strip()

    if choice == "1":
        # Overview: a few headline numbers about all my purchases
        print("Purchases:", len(df))                                   # number of rows
        print("Total spent: €", round(df["price"].sum(), 2))           # add up every price
        print("Average purchase: €", round(df["price"].mean(), 2))     # average price
        # daily_totals includes the days I spent nothing, so this is the true average per day
        print("Average spent per day: €", round(analysis.daily_totals(df).mean(), 2))

    elif choice == "2":
        # Show total and average spending grouped by each of these four columns
        for column in ["category", "need_want", "payment", "online_or_in_person"]:
            print("\nBy", column)
            print(analysis.total_by(df, column))

    elif choice == "3":
        # Average spent per day: weekends vs weekdays, then for each day of the week
        print(analysis.weekend_vs_weekday(df))
        print(analysis.spending_by_weekday(df))

    elif choice == "4":
        # try/except stops the program crashing if I type letters instead of a number
        try:
            amount = float(input("Show purchases over how many euro? "))
            # Keep only rows where the price is bigger than my amount, biggest first
            show(df[df["price"] > amount].sort_values("price", ascending=False))
        except ValueError:
            print("Please type a number, like 50")

    elif choice == "5":
        # Show the list of categories so I know what I can type
        print("Categories:", ", ".join(sorted(df["category"].unique())))
        name = input("Which category? ").strip()
        # Compare in lowercase so "food", "Food" and "FOOD" all work
        show(df[df["category"].str.lower() == name.lower()])

    elif choice == "0":
        break   # stops the while loop, so the program ends

    else:
        # Anything else I type (letters, empty, a wrong number)
        print("Please type a number from 0 to 5.")