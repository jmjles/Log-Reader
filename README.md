Log Reader
=============
Requirments
------------

Python 3.0, Vagrant, and VMBox are *needed* to run this code.

Initializing
-------------

Once you have all the files downloaded and put into a folder, run the following code:      
`vagrant init`  
`vagrant up`  
`cd /vagrant`  
`psql -d news -f newsdata.sql`  
   
This will set up vagrant and the database for you.  
As for running the __actual code__,please input the following code:  
`python dbnews.py`  

Usage
-----
`dbnews.py` is the source code, it makes everything happen.  
`newsdata.sql` is the database.