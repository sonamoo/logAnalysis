# logAnalysis
This python DB-API analyses the top four most viewed articles authors, and the day and the HTTP status error percentage. 

## How to run
- [Install PostgreSQL](https://www.postgresql.org/download/macosx/)
- unzip newsdata.sql.zip file
- on the terminal run `python logs_analysis.py`

## Example display

============== top 4 articles ==============
Candidate is jerk, alleges rival   :  338647
Bears love berries, alleges bear   :  253801
Bad things gone, say good people   :  170098
Goats eat Google's lawn            :   84906

============== top 4 authors ===============
Ursula La Multa                    :  507594
Rudolf von Treppenwitz             :  423457
Anonymous Contributor              :  170098
Markoff Chaney                     :   84557

======= higher than 1 percent req err ========
2016-07-17 --- 2.2626862468 % error
