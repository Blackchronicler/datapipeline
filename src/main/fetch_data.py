class FetchData:
    
    def __init__(self, conn, db_table : str) -> None:
        self.conn = conn
        self.db_table = db_table

    def _fetch_data(self):
        """ Check data availability in the DB """

        sample_db = 0
        cur = self.conn.cursor()
        try:
            print(f"This are the results of the query made to the table \"{str(self.db_table)}\".", "\n", sep="")
            cur.execute(f"SELECT * FROM {self.db_table};")
            sample_db = cur.fetchall()
            self.conn.commit()
            return  sample_db
        
        except Exception as e:
            print(f"Error while fetching data: {str(e)}")
            self.conn.rollback()
            return 1
        
        
    def _show_results(self):
        """ Preview into the data from the DB """
        
        try:
            results = self._fetch_data()
            for record in results[:10]:     # Adjust results limit according to needs
                print(record)
                
        except Exception as e:
            print(f"Preview of the results unavailable due to this error: {str(e)}")
            exit(1)
