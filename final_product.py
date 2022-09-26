# Importing necessary libraries
import pandas as pd

from connect_to_db import ConnectToDatabase
import create_tables_db
from git_crawler import GitCrawler as gc
from load_db import PopulateDatabase
from fetch_data import FetchData

#orgs_wanted = ["facebook", "ubuntu", "OSGeo"]
orgs_wanted = ["facebook", "netflix", "twitter", "adobe", "ubuntu", "OSGeo"]
database_tables = ["languages", "organisation"]

# Connection to Database
conn = ConnectToDatabase._connecting_to_db()

# Create database tables required
create_tables_db.main(conn)

# Crawl Github
# df_orgs = gc(orgs_wanted[5])._getting_organisation_details()
# df_langs = gc(orgs_wanted[5])._getting_languages_used()

# Load database tables
df_orgs = []
df_langs = []
for org in orgs_wanted:
    print(f"Fetching data from {org}.")
    df_orgs.append(gc(org)._getting_organisation_details())
    df_langs.append(gc(org)._getting_languages_used())

all_df_orgs = pd.concat(df_orgs, axis=0)
all_df_orgs = all_df_orgs.reset_index(drop=True)
PopulateDatabase(conn, all_df_orgs, database_tables[1])._populate_db()

all_df_langs = pd.concat(df_langs, axis=0)
all_df_langs = all_df_langs.reset_index(drop=True)
PopulateDatabase(conn, all_df_langs, database_tables[0])._populate_db()


# for org in orgs_wanted:
# df_orgs = gc(org)._getting_organisation_details()
# df_langs = gc(org)._getting_languages_used()
# PopulateDatabase(conn, df_langs, database_tables[0])._populate_db()
# PopulateDatabase(conn, df_orgs, database_tables[1])._populate_db()


if __name__ == "__main__":
    # Fetch data from database
    FetchData(conn, database_tables[0])._show_results()
    FetchData(conn, database_tables[1])._show_results()
    print(all_df_orgs)
    print(all_df_langs)

    #print(all_df_orgs.tail())
