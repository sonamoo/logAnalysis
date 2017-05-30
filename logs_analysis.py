import psycopg2


def connect(database_name="news"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print "failed to connect to the database"


def createViewsForTopArticles():
    db, cursor = connect()
    # First drop the existence top_articles view.
    cursor.execute("DROP VIEW top_articles;")
    QUERY = "CREATE VIEW top_articles AS " \
            "SELECT substring(path, 10, 100) AS article, "\
            "COUNT(path) as views "\
            "FROM log " \
            "GROUP BY article " \
            "ORDER BY views desc " \
            "OFFSET 1 " \
            "LIMIT 4;"
    cursor.execute(QUERY)
    db.commit()
    db.close()


def displayFourPopularArticles():
    """display four popular articles"""
    db, cursor = connect()
    createViewsForTopArticles()
    QUERY = "SELECT articles.title, top_articles.views " \
            "FROM articles, top_articles " \
            "WHERE articles.slug = top_articles.article " \
            "ORDER BY views DESC;"
    cursor.execute(QUERY)
    articles = cursor.fetchall()
    db.close()
    print '============== top 4 articles =============='
    for a, b in articles:
        print '{0:35s}: {1:7n}'.format(a, b)
    print ''


def createViewsForTopAuthors():
    """
    Create the necessary views to query
    top authors with the number of views
    """
    db, cursor = connect()
    cursor.execute("DROP VIEW title_views CASCADE;")
    QUERY = "CREATE VIEW title_views AS " \
            "SELECT SUBSTRING(path, 10, 100) AS title, COUNT(path) AS views " \
            "FROM log " \
            "GROUP BY title " \
            "ORDER BY views DESC;"
    cursor.execute(QUERY)
    db.commit()
    QUERY = "CREATE view author_views AS " \
            "SELECT articles.author, SUM(title_views.views) AS author_views " \
            "FROM title_views, articles " \
            "WHERE articles.slug = title_views.title " \
            "GROUP BY author " \
            "ORDER BY author_views DESC;"
    cursor.execute(QUERY)
    db.commit()
    db.close()


def displayTopAuthors():
    """Displays the top four authors with number of views"""
    db, cursor = connect()
    createViewsForTopAuthors()
    QUERY = "SELECT authors.name AS author, "\
            "author_views.author_views AS views "\
            "FROM authors, author_views "\
            "WHERE authors.id = author_views.author;"
    cursor.execute(QUERY)
    author_views = cursor.fetchall()
    db.close()
    print '============== top 4 authors ==============='
    for a, b in author_views:
        print '{0:35s}: {1:7n}'.format(a, b)
    print ''


def createViewsForReqErr():
    """Creates four views that are necessary to list err percent."""
    db, cursor = connect()
    cursor.execute("DROP VIEW view_err_rate;")
    cursor.execute("DROP VIEW view_status;")
    cursor.execute("DROP VIEW view_total_notfound;")
    cursor.execute("DROP VIEW view_total_status;")

    QUERY = "CREATE VIEW view_total_notfound AS " \
            "SELECT DATE(time) AS day, COUNT(*) AS total_404 " \
            "FROM log " \
            "WHERE status = '404 NOT FOUND' " \
            "GROUP BY day order by day;"
    cursor.execute(QUERY)
    db.commit()
    QUERY = "CREATE VIEW view_total_status AS "\
            "SELECT DATE(time) AS day, COUNT(*) AS total_status "\
            "FROM log "\
            "GROUP BY day "\
            "ORDER BY day;"
    cursor.execute(QUERY)
    db.commit()
    QUERY = "CREATE VIEW view_status AS "\
            "SELECT view_total_status.day AS day, "\
            "view_total_status.total_status AS reqs, "\
            "view_total_notfound.total_404 AS bad_reqs "\
            "FROM view_total_status, view_total_notfound "\
            "WHERE view_total_status.day = view_total_notfound.day;"
    cursor.execute(QUERY)
    db.commit()

    QUERY = "CREATE VIEW view_err_rate AS "\
            "SELECT day, "\
            "(CAST(bad_reqs AS FLOAT)/CAST(reqs AS FLOAT) * 100) "\
            "AS err_percent "\
            "FROM view_status "\
            "ORDER BY day;"
    cursor.execute(QUERY)
    db.commit()
    db.close()


def displayHighErr():
    """
    Displays the day with error rate on when
    not found status rate was higher than 1%
    """
    db, cursor = connect()
    createViewsForReqErr()
    QUERY = "SELECT day, err_percent FROM view_err_rate WHERE err_percent > 1;"
    cursor.execute(QUERY)
    db.commit()
    day_and_err_rate = cursor.fetchall()
    db.close()
    print '======= higher than 1 percent req err ========'
    for a, b in day_and_err_rate:
        print a, "---", b, "% error"


displayFourPopularArticles()
displayTopAuthors()
displayHighErr()
