# Importing necessary libraries
from io import StringIO
from connect_to_db import ConnectToDatabase as cd
from git_crawler import GitCrawler as gc


class PopulateDatabase:

    def __init__(self, conn, df, table_name: str) -> None:
        self.conn = conn
        self.df = df
        self.table_name = table_name

    def _populate_db(self):
        """ While populating DB, we will save the dataframe in memory and then copy it to the table """
        buffer = StringIO()  # used to save df in memmory
        self.df.to_csv(buffer, index_label='id', header=False)
        buffer.seek(0)
        cur = self.conn.cursor()
        try:
            cur.copy_from(buffer, self.table_name, sep=",")
            self.conn.commit()
            print(f"Data has been uploaded to the table: {self.table_name} in the DB. :D ")

        except Exception as e:
            print(f"Error while populating table(s): {str(e)}")
            self.conn.rollback()


if __name__ == "__main__":
    PopulateDatabase(cd._connecting_to_db(), gc("OSGeo")._getting_organisation_details(), "organisation")._populate_db()
