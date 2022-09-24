# Importing necessary libraries
from connect_to_db import ConnectToDatabase
import create_tables_db
from git_crawler import GitCrawler as gc
from load_db import PopulateDatabase
from fetch_data import FetchData

orgs_wanted = ["facebook", "netflix", "twitter", "adobe", "ubuntu", "OSGeo"]
database_tables = ["languages", "organisation"] 

# Connection to Database
conn = ConnectToDatabase._connecting_to_db()

# Create database tables required
create_tables_db.main(conn)

# Crawl Github
df_orgs = gc(orgs_wanted[5])._getting_organisation_details()
df_langs = gc(orgs_wanted[5])._getting_languages_used()

# Load database tables
PopulateDatabase._populate_db(conn, df_langs, database_tables[0])
PopulateDatabase._populate_db(conn, df_orgs, database_tables[1])

# Fetch data from database
FetchData._show_results(conn, database_tables[0])

if __name__ == "__main__":
    df_orgs
    