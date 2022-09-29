from unittest import result


class SampleData:
    
    def __init__(self, conn, db_table : str) -> None:
        self.conn = conn
        self.db_table = db_table

    def _sample_data(self):
        """ Check data availability in the DB """
        
        sample_db = 0
        cur = self.conn.cursor()
        try:
            print(f"This are the results of the query made to the table \"{str(self.db_table)}\".", "\n", sep="")
            cur.execute(f"SELECT * FROM {self.db_table};")
            sample_db = cur.fetchall()
            cur.close()
            return sample_db
        
        except Exception as e:
            print(f"Error while fetching data: {str(e)}")
            self.conn.rollback()
            cur.close()
            return 1

    def _show_results(self):
        """ Preview into the data from the DB """
        
        try:
            results = self._sample_data()
            print(results)
            # for record in results[:10]:     # Adjust results limit according to needs
            #     print(record)
                
        except Exception as e:
            print(f"Preview of the results unavailable due to this error: {str(e)}")
            exit(1)
            
if __name__ == "__main__":
    from connect_to_db import ConnectToDatabase
    conn = ConnectToDatabase._connecting_to_db()
    SampleData(conn, "languages")._show_results()