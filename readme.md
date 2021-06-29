Link to live project: https://cloudproject-bcd.herokuapp.com/
Youtube link of full explanation : https://youtu.be/RUCk3j8eG-g

Architecture:
![alt text]()

This code is ready to deploy on heroku. To run this code in local 
environment please follow the steps given in the report to 
undo all the changes done to the code to deploy on heroku.

Steps to run of local environment:

1) Undo all changes done to deploy on heroku
	1.1) Remove white noise from middleware
	1.2) Redefine static file path
	1.3) Delete Procfile
	1.4) Change allowed host in setting.py to '*'

2) cd to the present directory of this readme.txt file
3) run command 'py manage.py makemigrations'
4) run command 'py manage.py migrate'
5) run command 'py manage.py runserver'
6) Go to the URL provided in the terminal
7) The webapp is working. 

---------------------------Queue Service------------------------------
To view the data present in Club and Event Queue simply run the following
files:

1) clubreceiver.py  - This code receives data from club queue
2) emailreceiver.py - This code receives data from event queue

------------------------------Deployment----------------------------------
To deploy this code on any other environment follow the steps provided in
the report.

-------------------------Data Handling------------------------------------
To view data handlers , each app has a datahandler.py file ehich contains
all the necessary files and setting required to fetch and integrated
various database services.

Enjoy Coding !!
