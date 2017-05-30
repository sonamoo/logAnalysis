# logAnalysis
This python DB-API analyses the top four most viewed articles authors, and the day and the HTTP status error percentage. 

## How to run
- [Install PostgreSQL](https://www.postgresql.org/download/macosx/)
- unzip newsdata.sql.zip file
- on the terminal run `python logs_analysis.py`

## Example display

============== top 4 articles ==============__
Candidate is jerk, alleges rival   :  338647__
Bears love berries, alleges bear   :  253801__
Bad things gone, say good people   :  170098__
Goats eat Google's lawn            :   84906__
											__
============== top 4 authors ===============__
Ursula La Multa                    :  507594__
Rudolf von Treppenwitz             :  423457__
Anonymous Contributor              :  170098__
Markoff Chaney                     :   84557__
											__
======= higher than 1 percent req err ========__
2016-07-17 --- 2.2626862468 % error__
