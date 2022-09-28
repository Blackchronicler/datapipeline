# Importing necessary libraries
import psycopg2
import env as env_var

class ConnectToDatabase:
    
    def __init__(self) -> None:
        pass

    def _connecting_to_db():
        """ Connect to the PostgreSQL database server """

        ## Getting PAT for auth @ Database
        user_token = env_var.DB_USER
        pwd_token = env_var.DB_PASSWORD
        
        # Connection details
        db_parameters = {
        "host" : "localhost",
        "dbname" : "wsl",
        "user" : user_token,
        "password" : pwd_token,
        "port" : 5432,
        "options" : "-c search_path=dbo,github"  # Choosing which schemata one wants
        }
        
        try:
            print("\n", "Connecting to the PostgreSQL database...Please wait...", "\n", sep="")
            conn= psycopg2.connect(**db_parameters)
            print("Connection successful :) ", "\n", sep="")
            return conn

        except Exception as e:
            print(f"Sorry, the connection to the database was unsuccessful because: {str(e)}")
            exit(1)