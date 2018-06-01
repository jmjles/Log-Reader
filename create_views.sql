create view tbdef as select authors.name,articles.title,articles.slug,log.path,log.time,log.status from authors inner join articles on articles.author = authors.id inner join log on log.path = '/article/'||articles.slug; 
create view nttl as select count(log.time = log.time) as nottl from log where status = '404 NOT FOUND';
create view ttl as select count(log.time = log.time)as totl from log;
create view perc as select totl * 0.01 as percy from ttl;