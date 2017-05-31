\connect news;
DROP VIEW IF EXISTS author_views;
DROP VIEW IF EXISTS title_views;
DROP VIEW IF EXISTS top_articles;
DROP VIEW IF EXISTS view_err_rate;
DROP VIEW IF EXISTS view_status;
DROP VIEW IF EXISTS view_total_notfound;
DROP VIEW IF EXISTS view_total_status;

CREATE VIEW top_articles AS 
SELECT substring(path, 10, 100) AS article, COUNT(path) as views 
FROM log 
GROUP BY article 
ORDER BY views DESC OFFSET 1 
LIMIT 3;

CREATE VIEW title_views AS 
SELECT substring(path, length('/article/') + 1) AS title, COUNT(path) AS views 
FROM log 
GROUP BY title 
ORDER BY views DESC;

CREATE view author_views AS 
SELECT articles.author, SUM(title_views.views) AS author_views 
FROM title_views, articles 
WHERE articles.slug = title_views.title 
GROUP BY author 
ORDER BY author_views DESC;

CREATE VIEW view_total_notfound AS 
SELECT DATE(time) AS day, COUNT(*) AS total_404 
FROM log 
WHERE status = '404 NOT FOUND' 
GROUP BY day 
ORDER BY day;

CREATE VIEW view_total_status AS 
SELECT DATE(time) AS day, COUNT(*) AS total_status 
FROM log 
GROUP BY day 
ORDER BY day;

CREATE VIEW view_status AS 
SELECT view_total_status.day AS day, 
view_total_status.total_status AS reqs, 
view_total_notfound.total_404 AS bad_reqs 
FROM view_total_status, view_total_notfound 
WHERE view_total_status.day = view_total_notfound.day;
CREATE VIEW view_err_rate 
AS SELECT day, (CAST(bad_reqs AS FLOAT)/CAST(reqs AS FLOAT) * 100) AS err_percent 
FROM view_status 
ORDER BY day;