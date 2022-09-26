# Importing necessary libraries
import psycopg2
from git_crawler import Git_Crawler as gc
from io import StringIO
import pandas as pd

# Connection details
db_parameters = {
    "host" : "localhost",
    "database" : "development",
    "user" : gc.access_tokens[2],
    "password" : gc.access_tokens[3],
    "port_id" : 5432 }
conn = None

def _connecting_to_db(db_parameters):
    """ Connect to the PostgreSQL database server """
    
    conn = None
    try:
        print("Connecting to the PostgreSQL database...")
        conn= psycopg2.connect(**db_parameters)

    except Exception as e:
        print(f"Here is the problem with database connection: {str(e)}")

    print("Connection successful :) ")
    
    return conn

database_tables = ["orga_langs", "languages", "organisation"]

def _delete_tables_db(conn, list_of_tables):
    """ Delete all tables in database """
    
    cur = conn.cursor()
    try:
        for table in list_of_tables:
            cur.execute(f"DROP TABLE IF EXISTS {table};")
        conn.commit()
    
    except Exception as e:
        print(f"Error while deleting table(s): {str(e)}")
        conn.rollback()
        cur.close()
    
    cur.close()    
    print("All tables have been deleted from the database!!")
    
    
create_queries_dict = {
"create_organisation_table" : """ CREATE TABLE IF NOT EXISTS organisation (
                                orga_id int NOT NULL PRIMARY KEY,
                                organisation_name varchar(100) NOT NULL,
                                number_of_members int NOT NULL,
                                number_of_repositories int NOT NULL,
                                number_of_languages int NOT NULL); """,

"create_language_table" : """ CREATE TABLE IF NOT EXISTS languages (
                                    lang_id int NOT NULL PRIMARY KEY,
                                    language_typ varchar(100) NOT NULL,
                                    number_of_bytes int NOT NULL,
                                    organisation_name varchar(100) NOT NULL); """,
                                    
"create_orga_lang_table" : """ CREATE TABLE IF NOT EXISTS orga_langs (
                                    orga_langs_id int NOT NULL PRIMARY KEY,
                                    organisation_id int NOT NULL REFERENCES organisation(orga_id),
                                    language_typ_id int NOT NULL REFERENCES languages(lang_id)); """
}

def _create_tables_db(conn, dict_of_queries):
    """ Create tables in the database """
    
    cur = conn.cursor()
    try:
        for query in dict_of_queries:
            cur.execute(dict_of_queries[query])
        conn.commit()
        
    except Exception as e:
        print(f"Error while creating table(s): {str(e)}")
        conn.rollback()
        cur.close()
    
    cur.close()
    print("Tables now available in DB.")


df_langs = gc("OSGeo")._getting_languages_used()  ####adjust this
df_orgs = gc("OSGeo")._getting_organisation_details()  ####adjust this

def _populate_db(conn, df, table_name):
    """ Here we are going save the dataframe in memory and then copy it to the table """
    
    buffer = StringIO()   #used to save df in memmory
    df.to_csv(buffer, index_label='id', header=False)
    buffer.seek(0)
    cur = conn.cursor()
    try:
        cur.copy_from(buffer, table_name, sep=",")
        conn.commit()
        
    except Exception as e:
        print(f"Error while populating table(s): {str(e)}")
        conn.rollback()
        cur.close()

    cur.close()
    print("Copying into table(s) is done.")

def _sampling_db(conn, list_of_tables):
    """ Check that the values were inserted """
    sample_db= 0
    cur = conn.cursor()
    try:
        for table in list_of_tables:
            cur.execute(f"SELECT COUNT(*) FROM {table};")
        conn.commit()
        sample_db = cur.fetchall()
    
    except Exception as e:
        print(f"Error while deleting table(s): {str(e)}")
        conn.rollback()
        cur.close()
        
    return  sample_db
    
if conn is not None:
     conn.close()
     