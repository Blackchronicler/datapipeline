# Importing necessary libraries
import psycopg2
from git_crawler import Git_Crawler as gc

#Postgres details
hostname = "localhost"
database = "development"
username = gc.access_tokens[2]
pwd = gc.access_tokens[3]
port_id = 5432

try:
    conn= psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)

    conn.close()
    
except Exception as e:
    print (f"The connection to the database has the following problem: {str(e)}")