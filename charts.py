import matplotlib.pyplot as plt
import analysis


def chart_daily(df):
    """Line chart: how much I spent each day."""
    daily = analysis.daily_totals(df)
    plt.figure(figsize=(10, 5))
    plt.plot(daily.index, daily.values, marker="o")
    plt.title("Money spent each day")
    plt.xlabel("Date")
    plt.ylabel("Spent (€)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("chart_daily.png")


def chart_categories(df):
    """Bar chart: total spent in each category."""
    totals = analysis.total_by(df, "category")["total"].sort_values()
    plt.figure(figsize=(8, 5))
    plt.barh(totals.index, totals.values)
    plt.title("Total spent by category")
    plt.xlabel("Spent (€)")
    plt.tight_layout()
    plt.savefig("chart_categories.png")


def chart_weekdays(df):
    """Bar chart: average spent on each day of the week."""
    average = analysis.spending_by_weekday(df)
    plt.figure(figsize=(8, 5))
    plt.bar(average.index, average.values)
    plt.title("Average spent on each day of the week")
    plt.ylabel("Average spent per day (€)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("chart_weekdays.png")


def chart_online_vs_in_person(df):
    """Bar chart: online vs in person spending."""
    totals = analysis.total_by(df, "online_or_in_person")["total"]
    plt.figure(figsize=(6, 5))
    plt.bar(totals.index, totals.values)
    plt.title("Online vs in person spending")
    plt.ylabel("Total spent (€)")
    plt.tight_layout()
    plt.savefig("chart_online_vs_in_person.png")


def chart_price_distribution(df):
    """Histogram: how big are my purchases?"""
    plt.figure(figsize=(8, 5))
    plt.hist(df["price"], bins=15)
    plt.title("How big are my purchases?")
    plt.xlabel("Price of one purchase (€)")
    plt.ylabel("Number of purchases")
    plt.tight_layout()
    plt.savefig("chart_price_distribution.png")


def chart_need_want(df):
    """Stacked bar chart: needs and wants inside each category."""
    table = analysis.need_want_by_category(df)
    table.plot(kind="barh", stacked=True, figsize=(8, 5))
    plt.title("Needs and wants in each category")
    plt.xlabel("Spent (€)")
    plt.tight_layout()
    plt.savefig("chart_need_want.png")


if __name__ == "__main__":
    df = analysis.load_data()
    chart_daily(df)
    chart_categories(df)
    chart_weekdays(df)
    chart_online_vs_in_person(df)
    chart_price_distribution(df)
    chart_need_want(df)
    plt.show()   # shows all the charts at once