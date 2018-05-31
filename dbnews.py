import psycopg2
conn = psycopg2.connect(dbname="news")
cursor = conn.cursor()
# Creates views needed to answer the following questions.
query = ("create view tbdef as select authors.name,articles.title,articles.slug,log.time,log.status from authors inner join articles on articles.author = authors.id inner join log on log.path ~ articles.slug;")
cursor.execute(query)
query = ("create view ttl as select count(log.time) as totl from log;")
cursor.execute(query)
# This code is currently redundant, but keeping it here if it is needed later.
# query = ("create view perc as select totl * 0.01 as percy from ttl;")
# cursor.execute(query)

# Asks for data fromthe database.
print ("What are the most popular three articles of all time?")
print ("")
query = ("select tbdef.title,count(tbdef.slug) from tbdef group by title order by title desc limit 3;")
# Runs the folloing code from the query.
cursor.execute(query)
# Gets the results from the query and prints them in an orderly fashion.
results = cursor.fetchall()
for row in results:
    print (row)

print ("")
print ("Who are the most popular article authors of all time?")
print ("")
query = ("select tbdef.name,count(tbdef.slug) from tbdef group by name order by name desc limit 3;")
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print (row)

# Not working(W.I.P)
print ("")
print ("In which days did more than 1% of requests lead to errors?")
print ("")
query = ("select tbdef.time from tbdef where tbdef.time = tbdef.time and tbdef.status = '404 NOT FOUND' order by tbdef.time desc limit 30 offset 16777.35;")
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print (row)
# There is nothing else to be done, so now we close the connection to the database.
conn.close()
