# Importing necessary llibraries
from git_crawler import Git_Crawler as gc
import psycopg2

class ConnectToDatabase:
    
    def __init__(self) -> None:
        pass

    def _connecting_to_db():
        """ Connect to the PostgreSQL database server """
        
        # Connection details
        db_parameters = {
        "host" : "localhost",
        "database" : "development",
        "user" : gc.access_tokens[2],
        "password" : gc.access_tokens[3],
        "port" : 5432 }
        
        try:
            print("Connecting to the PostgreSQL database...")
            conn= psycopg2.connect(**db_parameters)
            print("Connection successful :) ")
            return conn

        except Exception as e:
            print(f"Connection to database was unsuccessful because: {str(e)}")
        
## Testing Stuff -> to be deleted
if __name__ == "__main__":
    ConnectToDatabase._connecting_to_db()