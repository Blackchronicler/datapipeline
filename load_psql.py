# Importing necessary libraries
import psycopg2
from git_crawler import Git_Crawler as gc

#Connection details
hostname = "localhost"
database = "development"
username = gc.access_tokens[2]
pwd = gc.access_tokens[3]
port_id = 5432
cur = None
conn = None

try:
    conn= psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)
    
    cur = conn.cursor()
    
    create_organisation

except Exception as e:
    print (f"The connection to the database has the following problem: {str(e)}")
    
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()