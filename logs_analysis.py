#!/usr/bin/env python
import psycopg2


def connect(database_name="news"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print "failed to connect to the database"


def displayFourPopularArticles():
    """display four popular articles"""
    db, cursor = connect()
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


def displayTopAuthors():
    """Displays the top four authors with number of views"""
    db, cursor = connect()
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


def displayHighErr():
    """
    Displays the day with error rate on when
    not found status rate was higher than 1%
    """
    db, cursor = connect()
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
