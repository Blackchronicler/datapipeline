# Importing necessary libraries
from io import StringIO
from packages.connect_to_db import ConnectToDatabase as cd

class PopulateDatabase:
    
    def __init__(self, df, table_name : str) -> None:
        self.df = df
        self.table_name = table_name
    
    def _populate_db(self):
        """ While populating DB, we will save the dataframe in memory and then copy it to the table """
        
        buffer = StringIO()   #used to save df in memmory
        self.df.to_csv(buffer, index_label='id', header=False)
        buffer.seek(0)
        conn = cd._connecting_to_db()
        cur = conn.cursor()
        try:
            cur.copy_from(buffer, self.table_name, sep=",")
            conn.commit()
            print(f"Data has been uploaded to the table: {self.table_name} in the DB :D ")
            
        except Exception as e:
            print(f"Error while populating table(s): {str(e)}")
            conn.rollback()

        cur.close()
        conn.close()