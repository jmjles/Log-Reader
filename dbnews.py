#!/usr/bin/env python3
import psycopg2
conn = psycopg2.connect(dbname="news")
cursor = conn.cursor()
# Asks for data from the database.
print ("What are the most popular three articles of all time?")
print ("")
query = ("select tbdef.title,count(tbdef.slug) as views from tbdef group by title order by views desc limit 3;")
# Runs the folloing code from the query.
cursor.execute(query)
# Gets the results from the query and prints them in an orderly fashion.
results = cursor.fetchall()
for row in results:
    print ('"{}"--{} views'.format(row[0],row[1]))

print ("")
print ("Who are the most popular article authors of all time?")
print ("")
query = ("select tbdef.name,count(tbdef.slug) as views from tbdef group by name order by views desc limit 3;")
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print ('{}--{} views'.format(row[0],row[1]))

# Not working(W.I.P)
print ("")
print ("In which days did more than 1% of requests lead to errors?")
print ("")
query = ("select time,count(time) from log,ttl,perc,nttl where status='404 NOT FOUND' and nottl < percy group by time order by time limit 1;")
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print ('{}--{}% errors'.format(row[0],row[1]))
# There is nothing else to be done, so now we close the connection to the database.
conn.close()
