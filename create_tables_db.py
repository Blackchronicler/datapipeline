#  Tables and queries for database
database_tables = ["org_langs", "languages", "organisation"]
create_queries = {
"create_organisation_table" : """ CREATE TABLE IF NOT EXISTS organisation (
                                org_id int NOT NULL PRIMARY KEY,
                                organisation_name varchar(100) NOT NULL,
                                number_of_members int NOT NULL,
                                number_of_repositories int NOT NULL,
                                number_of_languages int NOT NULL); """,

"create_language_table" : """ CREATE TABLE IF NOT EXISTS languages (
                                    lang_id int NOT NULL PRIMARY KEY,
                                    language_typ varchar(100) NOT NULL,
                                    number_of_bytes int NOT NULL,
                                    organisation_name varchar(100) NOT NULL); """,
                                    
"create_org_lang_table" : """ CREATE TABLE IF NOT EXISTS org_langs (
                                    org_langs_id int NOT NULL PRIMARY KEY,
                                    organisation_id int NOT NULL REFERENCES organisation(org_id),
                                    language_typ_id int NOT NULL REFERENCES languages(lang_id)); """
}

def delete_tables_db(conn):
    """ Delete all tables in database """
    
    cur = conn.cursor()
    try:
        for table in database_tables:
            cur.execute(f"DROP TABLE IF EXISTS {table};")
        conn.commit()    
        print("All tables have been deleted from the database!!", "\n", sep="")
    
    except Exception as e:
        print(f"Error while deleting table(s): {str(e)}")
        conn.rollback()
        return 1
    
    cur.close()

def create_tables_db(conn):
    """ Create tables in the database """
    
    cur = conn.cursor()
    try:
        for query in create_queries:
            cur.execute(create_queries[query])
        conn.commit()
        print("Table(s) successfully created in the database!! :D", "\n", sep="")
        
    except Exception as e:
        print(f"Error while creating table(s): {str(e)}")
        conn.rollback()
        return 1
    
    cur.close()
    
def main(conn):
    """ Executes the above """
    
    try:
        delete_tables_db(conn)
        create_tables_db(conn)
        
    except Exception as e:
        print(f"Error while running the main method in create_tables_db file: {str(e)}")
        exit(1)
    

if __name__ == "__main__":
    main()