# Data Centric Assignment


#### My project will be on money spent, I'll be tracking every cent I spend, where, when, how much, and a couple other necessary attributes.


## QUESTIONS TO ANSWER

Do I spend more money on weekends compared to weekdays?

Do I do more online shopping or in person shopping?

What category do I spend the most money on? (eg. shopping, sports, food).


## DATA DICTIONARY

|FIELD NAME        |       DATA TYPE       |      DESCRIPTION                   |                              EXAMPLES |
|---|---|---|---|
|Date              |       Date               |   Records the date on which the money was spent.           |    25/10                             |
|Price             |       Decimal            |   Records the amount spent, in euro.                       |    50.00, 94.38                      |
|Location          |       Text               |   Identifies the location at which the money was spent.    |    Amazon, Smyths Blanchardstown     |
|need/want         |       Categorical Text   |   Records if the expense was a necessity or a luxury.      |    need, want                        |
|cash/card         |       Categorical Text   |   Records if the payment was made via cash or card.        |    cash, card                        |
|Description       |       Text               |   Brief Details about what was purchased.                  |    Petrol for my car, Chicken kebab  |
|Category          |       Categorical Text   |   Groups money spent into more general categories.         |    food, fuel, furniture             |
|Online/in person  |       Categorical Text   |   Identifies whether the purchase was online or in person. |    online, in person                 |


# AFTER FINISHING MY PROJECT

## The dataset
File: Excel Data/Data Centric Assignment Data.csv
Size: 56 rows, 8 columns, 16/10/2026 to 16/11/2026 (32 days, 28 of them with purchases)
One row = one purchase. If I bought several things on one day, each purchase is its own row.
How I collected it: After each cash purchase, I would quickly write down the exact price and what I bought, then when I got home, seeing the note would jog my memory and I would remember where it was, and I would be able to fill in all columns.
After each card purchase, I didn't need to write it down as I could go home and check in my banking app, where I could see how much money I spent, and where


## Photos of me collecting data

<img width="735" height="1600" alt="WhatsApp Image 2026-10-22 at 10 27 35" src="https://github.com/user-attachments/assets/d84e8203-a807-48b7-8957-9f755894da76" />


### This is how i would record cash transactions, very brief, so you can see I would do it in a rush but directly in the moment

<img width="134" height="51" alt="Screenshot 2026-11-25 at 00 56 19" src="https://github.com/user-attachments/assets/9843ce35-b1a4-4386-a5de-d6e4e9a5e357" />





## problems, missing data and outliers

Days with no purchases: I recorded nothing on 01/11, 07/11, 09/11 and 14/11. In my analysis they count as €0.
Outliers: Two purchases are much bigger than the rest: €240 church membership fees (08/11) and €160 for a camp (02/11). They are real payments, so I kept them in the data.
Messy entries: My CSV had trailing spaces (for example Car  and  Circle K Hartstown) and inconsistent capitals (In person and in person). I left the CSV as I recorded it and cleaned the data when loading it into the database.

Cleaning on load basically just removes extra spaces, makes capital letters consistent, converts dates to a format SQL can sort, removes rows missing a date or price, and warns about prices over €150.




## How the project works
|File	| What it does|
|---|---|
|load_data.py |	Reads the CSV, cleans it, checks the values and puts it into the SQLite database spending.db|
|queries.py |	SQL queries (COUNT, SUM, AVG, GROUP BY, ORDER BY, WHERE)|
|analysis.py |	pandas functions that answer questions about the data|
|charts.py |	matplotlib charts|
|main.py |	The menu to explore the data|

## Charts

<img width="800" height="500" alt="chart_categories" src="https://github.com/user-attachments/assets/a5603f58-1be2-4317-b3f9-4b3fbcb4d00e" />


<img width="1000" height="500" alt="chart_daily" src="https://github.com/user-attachments/assets/cf4cbc98-8374-4487-8898-be339815ce19" />


<img width="800" height="500" alt="chart_need_want" src="https://github.com/user-attachments/assets/28b23165-d84f-4e7f-86de-c930c9709a0c" />


<img width="600" height="500" alt="chart_online_vs_in_person" src="https://github.com/user-attachments/assets/842ee85b-eb73-4ccb-ba85-018d9decc8de" />


<img width="800" height="500" alt="chart_price_distribution" src="https://github.com/user-attachments/assets/cb404fae-cc82-4da8-91d5-aea5ac2a0a06" />


<img width="800" height="500" alt="chart_weekdays" src="https://github.com/user-attachments/assets/e66a7b81-cdc4-4ec1-bfd7-88447d2fa044" />




