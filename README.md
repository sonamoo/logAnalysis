# logAnalysis
This python DB-API analyses large database with over a million rows. API analyses the top four most viewed articles authors, and the day and the HTTP status error percentage. 

## How to run
- [Install PostgreSQL](https://www.postgresql.org/download/macosx/)
- unzip newsdata.sql.zip file
- From the project folder run `psql -d news 
- run `CREATE VIEW top_articles AS SELECT substring(path, 10, 100) AS article COUNT(path) as views FROM log GROUP BY article GROUP BY article ORDER BY views desc OFFSET 1 LIMIT 3;`
- run `CREATE VIEW title_views AS SELECT SUBSTRING(path, 10, 100) AS title, COUNT(path) AS views FROM log GROUP BY title ORDER BY views DESC;`
- run `CREATE view author_views AS SELECT articles.author, SUM(title_views.views) AS author_views FROM title_views, articles WHERE articles.slug = title_views.title GROUP BY author ORDER BY author_views DESC;`
- run `CREATE VIEW view_total_notfound AS SELECT DATE(time) AS day, COUNT(*) AS total_404 FROM log WHERE status = '404 NOT FOUND' GROUP BY day order by day;`
- run `CREATE VIEW view_total_status AS SELECT DATE(time) AS day, COUNT(*) AS total_status FROM log GROUP BY day ORDER BY day;`
- run `CREATE VIEW view_status AS SELECT view_total_status.day AS day, view_total_status.total_status AS reqs, view_total_notfound.total_404 AS bad_reqs FROM view_total_status, view_total_notfound WHERE view_total_status.day = view_total_notfound.day;`
- run `CREATE VIEW view_err_rate AS SELECT day, (CAST(bad_reqs AS FLOAT)/CAST(reqs AS FLOAT) * 100) AS err_percent FROM view_status ORDER BY day;`
- run '\q' to exit the database
- on the terminal run `python logs_analysis.py`

## Views
There are 7 views are required to run this API.

| Name               | Columns        
| -------------      |-------------
| author_views       | author id, total views for author 
| title_views        | article slug, views of the slugqq
| top_articles       | top four article slug, views      
| view_err_rate      | day, rate of HTTP error (N of HTTP 404/ N of HTTP 200)  
| view_status        | day, number of total requests, number of total bad requests      
| view_total_notfound| day, number of total bad requests      
| view_total_status  | day, number of total requests    

## Example display

============== top 4 articles ==============<br/>
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
