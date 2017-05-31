# logAnalysis
This python DB-API analyses large database with over a million rows. API analyses the top three most viewed articles four authors, and the day that ad more than 1 % of HTTP request errors.

## How to run
- [Install PostgreSQL](https://www.postgresql.org/download/macosx/)
- unzip newsdata.sql.zip file
- run `psql -f logs_analysis.sql`
- run `python logs_analysis.py`

## Views
There are 7 views are required to run this API.

| Name               | Columns        
| -------------      |-------------
| author_views       | author id, total views for author 
| title_views        | article slug, views of the slug
| top_articles       | top four article slug, views      
| view_err_rate      | day, rate of HTTP error (N of HTTP 404/ N of HTTP 200)  
| view_status        | day, number of total requests, number of total bad requests      
| view_total_notfound| day, number of total bad requests      
| view_total_status  | day, number of total requests    

## Example display

============== top 3 articles ==============<br/>
Candidate is jerk, alleges rival   :  338647<br/>
Bears love berries, alleges bear   :  253801<br/>
Bad things gone, say good people   :  170098<br/>
											<br/>
============== top 4 authors ===============<br/>
Ursula La Multa                    :  507594<br/>
Rudolf von Treppenwitz             :  423457<br/>
Anonymous Contributor              :  170098<br/>
Markoff Chaney                     :   84557<br/>
											<br/>
======= higher than 1 percent req err ========<br/>
2016-07-17 --- 2.2626862468 % error<br/>
