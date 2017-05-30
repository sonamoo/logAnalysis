# logAnalysis
This python DB-API analyses the top four most viewed articles authors, and the day and the HTTP status error percentage. 

## How to run
- [Install PostgreSQL](https://www.postgresql.org/download/macosx/)
- unzip newsdata.sql.zip file
- on the terminal run `python logs_analysis.py`

## Example display

============== top 4 articles ==============<br/>
Candidate is jerk, alleges rival   :  338647<br/>
Bears love berries, alleges bear   :  253801<br/>
Bad things gone, say good people   :  170098<br/>
Goats eat Google's lawn            :   84906<br/>
											<br/>
============== top 4 authors ===============<br/>
Ursula La Multa                    :  507594<br/>
Rudolf von Treppenwitz             :  423457<br/>
Anonymous Contributor              :  170098<br/>
Markoff Chaney                     :   84557<br/>
											<br/>
======= higher than 1 percent req err ========<br/>
2016-07-17 --- 2.2626862468 % error<br/>
