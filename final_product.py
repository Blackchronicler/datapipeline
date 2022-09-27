# Importing necessary libraries
from scr.main.connect_to_db import ConnectToDatabase
import scr.main.create_tables_db as create_tables_db
from scr.main.git_crawler import GitCrawler
from scr.main.load_db import PopulateDatabase
from main.fetch_data import FetchData
import pandas as pd

# orgs_wanted = ["facebook", "netflix", "twitter", "adobe", "ubuntu", "OSGeo"]
orgs_wanted = ["OSGeo"]
database_tables = ["languages", "organisation"]

# Connection to Database
conn = ConnectToDatabase._connecting_to_db()

# Create database tables required
create_tables_db.main(conn)

# Crawl Github
df_orgs = []
df_langs = []

for org in orgs_wanted:
    print(f"Fetching data from {org}.", "\n", sep="")
    df_orgs.append(GitCrawler(org)._getting_organisation_details())
    df_langs.append(GitCrawler(org)._getting_languages_used())

# Combining all the dataframes to a single dataframe    
final_df_orgs = pd.concat(df_orgs, axis=0)
final_df_orgs = final_df_orgs.reset_index(drop=True)  # Organisation
final_df_langs = pd.concat(df_langs, axis=0)
final_df_langs = final_df_langs.reset_index(drop=True)  # Languages

# Load database tables
PopulateDatabase(final_df_langs, database_tables[0])._populate_db()
PopulateDatabase(final_df_orgs, database_tables[1])._populate_db()

# Fetch data from database
FetchData(database_tables[0])._show_results()
FetchData(database_tables[1])._show_results()
