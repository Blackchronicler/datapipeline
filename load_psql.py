# Importing necessary libraries
import psycopg2
from git_crawler import Git_Crawler as gc
from sqlalchemy import create_engine

# Connection details
hostname = "localhost"
database = "development"
username = gc.access_tokens[2]
pwd = gc.access_tokens[3]
port_id = 5432
cur = None
conn = None

# Accessing the database
try:
    conn= psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)
    
    cur = conn.cursor()
    
    # Clearing database
    database_tables = ["orga_langs", "languages", "organisation"]
    for table in database_tables:
        cur.execute(f"DROP TABLE IF EXISTS {table};")
        
    conn.commit()
    
    # Creating tables
    create_organisation_table = """ CREATE TABLE IF NOT EXISTS organisation (
                                        orga_id int NOT NULL PRIMARY KEY,
                                        organisation_name varchar(100) NOT NULL,
                                        number_of_members int NOT NULL,
                                        number_of_repositories int NOT NULL,
                                        number_of_languages int NOT NULL); """

    create_language_table = """ CREATE TABLE IF NOT EXISTS languages (
                                        lang_id int NOT NULL PRIMARY KEY,
                                        language_typ varchar(100) NOT NULL,
                                        number_of_bytes int NOT NULL,
                                        organisation_name varchar(100) NOT NULL); """
                                        
    create_orga_lang_table = """ CREATE TABLE IF NOT EXISTS orga_langs (
                                        orga_langs_id int NOT NULL PRIMARY KEY,
                                        organisation_id int NOT NULL REFERENCES organisation(orga_id),
                                        language_typ_id int NOT NULL REFERENCES languages(lang_id)); """
    
    new_database_tables = [create_organisation_table, create_language_table, create_orga_lang_table]
    for new_table in new_database_tables:
        cur.execute(new_table)
    
    conn.commit()
    
    # Inserting values into tables
    

except Exception as e:
    print (f"The connection to the database has the following problem: {str(e)}")
    
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()