from connect_to_db import ConnectToDatabase as cd
import pandas as pd
import seaborn as sns


class QueryData:
    
    conn = cd._connecting_to_db()
    cur = conn.cursor()

    def _barchart_org_infos(self, org):
        """ Getting details for barchart creation """
        
        try:
            query_holder = 0
            col_names = 0
            self.cur.execute(f"SELECT organisation_name, number_of_members, number_of_repositories, number_of_languages FROM github.organisation WHERE organisation_name = '{org}';")
            query_holder = self.cur.fetchall()
            col_names = self.cur.description
            self.cur.close()
            return pd.DataFrame(query_holder, 
                              index= [org], 
                              columns= pd.Index([x[0] for x in col_names], name = f"Organisation: {org}"))
        except Exception as e:
            print(f"Bar chart for this org not available because: {str(e)}")
            exit(1)
    
    def _get_langs_bytes(self, org):
        try:
            self.cur.execute(
                f"select language_typ, number_of_bytes from github.languages where organisation_name = '{org}' order by number_of_bytes desc")
            langs_bytes = self.cur.fetchall()
            return langs_bytes
        
        except Exception as e:
            print(e)
            return []

        # for lan_byte in lang_bytes:
        #    print(lan_byte)

    def _get_total_bytes(self, org):
        try:
            self.cur.execute(f"select sum(number_of_bytes) from public.languages where organisation_name = '{org}'")
            total = self.cur.fetchall()
            return total[0][0]
        
        except Exception as e:
            print(e)
            return -1




if __name__ == "__main__":
    results_data = QueryData()._barchart_org_infos("ubuntu")
    results_data.plot.bar()