# Importing necessary libraries
import psycopg2

class ConnectToDatabase:
    
    def __init__(self) -> None:
        pass

    def _connecting_to_db():
        """ Connect to the PostgreSQL database server """

        # Getting PAT for auth @ Database
        with open("pat.txt", "r") as f:
            access_tokens = f.readlines()
            user_token = access_tokens[2]
            pwd_token = access_tokens[3]
        
        # Connection details
        db_parameters = {
        "host" : "localhost",
        "database" : "development",
        "user" : user_token,
        "password" : pwd_token,
        "port" : 5432 }
        
        try:
            print("\n", "Connecting to the PostgreSQL database...Please wait...", "\n", sep="")
            conn= psycopg2.connect(**db_parameters)
            print("Connection successful :) ")
            return conn

        except Exception as e:
            print(f"Connection to database was unsuccessful because: {str(e)}")
            #exit(1)
            
if __name__ == "__main__":
    ConnectToDatabase._connecting_to_db()