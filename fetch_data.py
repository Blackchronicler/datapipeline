from connect_to_db import ConnectToDatabase as cd


class FetchData:

    def __init__(self, conn, db_table: str) -> None:
        self.conn = conn
        self.db_table = db_table

    def _fetch_data(self):
        """ Check data availability in the DB """

        sample_db = 0
        cur = self.conn.cursor()
        try:
            cur.execute(f"SELECT * FROM {self.db_table};")
            sample_db = cur.fetchall()
            self.conn.commit()
            return sample_db

        except Exception as e:
            print(f"Error while fetching data: {str(e)}")
            self.conn.rollback()

        cur.close()
        self.conn.close()

    def _show_results(self):
        """ Preview into the data from the DB """

        try:
            results = self._fetch_data()
            for record in results[:10]:  # Adjust results limit according to needs
                print(record)

        except Exception as e:
            print(f" Preview unavailable due to this error: {str(e)}")


if __name__ == "__main__":
    FetchData(cd._connecting_to_db(), "organisation")._show_results()
