##Project requirements:
* Python 2.7

###Software Required:

####Python Packages:
1. Flask
2. psycopg2
3. oauth2
4. sqlalchemy
5. oauth2client
6. requests
7. dicttoxml

####Database Requirements
This project supports both sqlite3 or postgres

####Additional Requirements
A **client_secrets.json** is need for oath with google, this need to downloaded from the google developers console. 

##Instructions to run the Project:
###Using Terminal:	
1. Open the terminal app in the current directory.
2. Install the library dicttoxml using the command "sudo pip install dicttoxml".
3. Create the database using the command "python database_setup".
4. Now, populate the database using "python populate_database.py".
5. Now, run "python project.py" to test the app.
6. Open the web browser and go the the url, "localhost:5000".