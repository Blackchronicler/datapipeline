# Importing necessary libraries
import psycopg2
from git_crawler import Git_Crawler as gc
from io import StringIO
import pandas as pd
from connect_to_db import ConnectToDatabase

# Connection to database
conn = ConnectToDatabase._connecting_to_db()
database_tables = ["org_langs", "languages", "organisation"]

def _delete_tables_db():
    """ Delete all tables in database """
    
    cur = conn.cursor()
    try:
        for table in database_tables:
            cur.execute(f"DROP TABLE IF EXISTS {table};")
        conn.commit()    
        print("All tables have been deleted from the database!!")
    
    except Exception as e:
        print(f"Error while deleting table(s): {str(e)}")
        conn.rollback()
    
    cur.close()
        

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

def _create_tables_db():
    """ Create tables in the database """
    
    cur = conn.cursor()
    try:
        for query in create_queries_dict:
            cur.execute(dict_of_queries[query])
        conn.commit()
        print("Tables successfully created in the database.")
        
    except Exception as e:
        print(f"Error while creating table(s): {str(e)}")
        conn.rollback()
    
    cur.close()

#df_langs = gc("OSGeo")._getting_languages_used()  ####adjust this
#df_orgs = gc("OSGeo")._getting_organisation_details()  ####adjust this

def _populate_db(df, table_name):
    """ While populating DB, we will save the dataframe in memory and then copy it to the table """
    
    buffer = StringIO()   #used to save df in memmory
    df.to_csv(buffer, index_label='id', header=False)
    buffer.seek(0)
    cur = conn.cursor()
    try:
        cur.copy_from(buffer, table_name, sep=",")
        conn.commit()
        print("Data has been uploaded to the DB. :D ")
        
    except Exception as e:
        print(f"Error while populating table(s): {str(e)}")
        conn.rollback()

    cur.close()


    
if conn is not None:
     conn.close()

## Testing Stuff -> to be deleted
if __name__ == "__main__":
    conn