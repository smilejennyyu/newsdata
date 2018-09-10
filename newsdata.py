#!/usr/bin/env python2.7
#
# Database access functions for the newsdata.
#

import psycopg2

DBNAME = "newsdata"


# To find the most popular three articles of all time
def most_popular_articles():
    textDoc = open("newsdata.txt", "w")
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    textDoc.write('Most popular three articles of all time:\n')
    cur.execute("SELECT a.title, count (g.path) as num\
                 FROM articles a \
                 RIGHT JOIN log g ON a.slug = SUBSTR(g.path, 10) \
                 WHERE SUBSTR(g.path, 10) != '' and a.title != 'None' \
                 GROUP BY a.title \
                 ORDER BY num DESC \
                 LIMIT 3;")
    results = cur.fetchall()
    for q1 in results:
        print "Query 1: ", q1[0], q1[1], "views"
        textDoc.write("{} -- {} views\n".format(str(q1[0]), str(q1[1])))
    db.close()


#To find the most popular three authors of all time
def most_popular_authors():
    textDoc = open("newsdata.txt", "a")
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    textDoc.write('\nMost popular three authors of all time:\n')
    cur.execute("SELECT authors.name, count(authors.name) as num \
                 FROM authors \
                 INNER JOIN articles ON authors.id = articles.author\
                 INNER JOIN log ON articles.slug = SUBSTR(log.path, 10) \
                 WHERE SUBSTR(log.path, 10) != '' \
                 and authors.name != 'Anonymous Contributor' \
                 GROUP BY authors.name \
                 ORDER BY num DESC \
                 LIMIT 3;")
    results = cur.fetchall()
    for q2 in results:
        print "Query 2: ", q2[0], q2[1], "views"
        textDoc.write("{} -- {} views\n".format(str(q2[0]), str(q2[1])))
    db.close()


#To find the days with more than 1% of requests lead to errors
def error_calculation():
    textDoc = open("newsdata.txt", "a")
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    textDoc.write('\nDays with more than 1% of requests lead to errors:\n')
    cur.execute("SELECT CAST(log.time AS DATE) as date, \
                 (count(case when log.status ='404 NOT FOUND' \
                 then 1 else null end) \
                 * 100.0 / count(log.status)) AS errorRate\
                 FROM log\
                 GROUP BY date\
                 HAVING count(case when log.status = '404 NOT FOUND' \
                 then 1 else null end) \
                 * 100.0 / count(log.status) > 1\
                 ORDER BY errorRate DESC;")
    results = cur.fetchall()
    for q3 in results:
        print "Query 3: ", str(q3[0]), str(round(q3[1], 2)), "%"
        textDoc.write("{} -- {}% errors\n".format(str(q3[0]), round(q3[1], 2)))
    db.close()

most_popular_articles()
most_popular_authors()
error_calculation()
