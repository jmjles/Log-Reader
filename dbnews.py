import psycopg2;
conn = psycopg2.connect(dbname="news");
cursor = conn.cursor();
query = ('select lead from articles');
cursor.execute(query);

results = cursor.fetchall();

print (results)

conn.close()
