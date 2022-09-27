# Importing necessary libraries
import psycopg2


class ConnectToDatabase:

    def __init__(self) -> None:
        pass

    def _connecting_to_db():
        """ Connect to the PostgreSQL database server """

        # Connection details
        db_parameters = {
            "host": "localhost",
            "dbname": "GithubCrawler",
            "user": "postgres",
            "password": "postgres",
            "port": 5432,
        }

        try:
            print("\n", "Connecting to the \"GitHubCrawler\" database...Please wait...", "\n", sep="")
            conn = psycopg2.connect(**db_parameters)
            print("Connection successful :) ", "\n", sep="")
            return conn

        except Exception as e:
            print(f"Sorry, the connection to the \"GitHubCrawler\" database was unsuccessful because: {str(e)}")
            exit(1)
