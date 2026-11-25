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


## The user interface
This is just a screenshot, I think it is much better to display it in action

<img width="244" height="313" alt="Screenshot 2026-11-25 at 01 20 33" src="https://github.com/user-attachments/assets/1fef564d-db49-4628-9707-446c0012672f" />



## Findings

I recorded 56 purchases totalling €2,211.66 over 32 days, which is about €69 a day (counting the days I bought nothing as €0).

### Question 1: 
Do I spend more on weekends than weekdays? Only slightly. I spent an average of €73.16 on each weekend day and €67.28 on each weekday. That is a small difference, and my biggest day of all was a Sunday (08/11, €257) mostly because of the €240 church fees, so one outlier payment brings the weekend average up. By day of the week, Monday was my most expensive (average €93.26) and Tuesday my cheapest (€46.18). 

### Question 2:
Do I do more online or in person shopping? In person, clearly. 40 of my 56 purchases (€1,634.68, 74% of the money) were in person, and 16 (€576.98, 26%) were online. The average purchase was similar: €40.87 in person and €36.06 online.


### Question 3:
What category do I spend the most money on? Activities was my biggest category (€472.46, 21%), mostly the church fees and the camp. Food came second (€374.01) but it was by far the most frequent: 24 purchases averaging only €15.58.


### Other things I found

A few big purchases matter a lot: the average purchase was €39.49.
The two outliers (€240 and €160) are 4% of my purchases but 18% of the money.

Needs vs wants: needs were 52% of what I spent (€1,144.57 over 33 purchases) and wants were 48% (€1,067.09 over 23 purchases).

Cash vs card: I paid by card more often (31 purchases, €892.54) but spent more in cash (25 purchases, €1,319.12), because most of the bigger expenses were cash.



## Limits of my data

The data collected was collected over a 4 week period, this doesn't give a big enough dataset to make accurate assumptions and predictions on. I think if I had collected 3 total months of spending, it would be much more accurate to how I usually spend my money, and more interesting to analyse.


## Reflection

Looking back at my spending analysis, I spent a lot more money than I had expected, however this is party due to the fact that I have just recently moved into our newly converted attic, which is now my bedroom, and I had to buy furniture for the room. It is also because I was 6 months late on monthly church membership fees, which would usually only be 30 euro per month, but I decided to pay it off until the end of the year. Also the bank holiday Monday in October brought my average spending up for Mondays very high, as I used that day off to buy furniture and skiing gear for a trip I am going on soon.




## Libraries Used
Libraries used: pandas, matplotlib and sqlite.


## References

https://youtu.be/byHcYRpMgI4?si=UaMqn-d3TAPJV0DK

https://youtu.be/Uh2ebFW8OYM?si=R2l_C_BsYMJ0uIJ_

https://youtu.be/q5uM4VKywbA?si=GXtuADfb1T6v-GbP

https://www.classcentral.com/classroom/youtube-learn-pandas-in-under-3-hours-filtering-joins-indexing-data-cleaning-visualizations-407307/675d1862bcf5e

https://www.youtube.com/watch?v=3Xc3CA655Y4

https://www.youtube.com/watch?v=huUg6wDUsv4

https://www.youtube.com/watch?v=8aW3tkIul-8

https://www.youtube.com/watch?v=RZMn7SsI9Yk
