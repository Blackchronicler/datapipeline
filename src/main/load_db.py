# Importing necessary libraries
from io import StringIO

class PopulateDatabase:
    
    def __init__(self, conn, df, table_name : str) -> None:
        self.df = df
        self.table_name = table_name
        self.conn = conn
    
    
    def _populate_db(self):
        """ While populating DB, we will save the dataframe in memory and then copy it to the table """
        
        buffer = StringIO()   #used to save df in memmory
        self.df.to_csv(buffer, index_label='id', header=False)
        buffer.seek(0)
        cur = self.conn.cursor()
        try:
            cur.copy_from(buffer, self.table_name, sep=",")
            self.conn.commit()
            print(f"Good news!! Data has been uploaded to the table: \"{str(self.table_name)}\" in the DB ;D ", "\n", sep="")
            
        except Exception as e:
            print(f"Error while populating table(s): {str(e)}")
            self.conn.rollback()
            return 1

        cur.close()
