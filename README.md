Log Reader
=============
This project's purpose is to read off specific data from a data base to answer questions by Udacity.
Requirments
------------

[Python 3.0](https://www.python.org/downloads/), [Vagrant](https://www.vagrantup.com/), and [VMBox](https://www.virtualbox.org/) are *needed* to run this code.

Initializing
-------------

Once you have all the files downloaded and put into a folder, unzip the newsdata.zip in the same directory as the rest of the files.  
Run the following code:      
`vagrant init`  
`vagrant up`  
`cd /vagrant`  
`psql -d news -f newsdata.sql` 
`psql - news -f create_views.sql`   
   
This will set up vagrant and the database for you.  
As for running the __actual code__,please input the following code:  
`python dbnews.py`  

Usage
-----
`dbnews.py` is the source code, it makes everything happen.  
`newsdata.sql` is the database.