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
