from git_crawler import GitCrawler as gc
from db import cur, conn


class Loader:
    org_list = ["facebook", "twitter", "netflix", "adobe", "ubuntu"]

    def __init__(self) -> None:
        print(f"Loading data from {self.org_list[:]}.")

    def _load_org_details(self, organisation):
        """ This function loads the organisation table in the database. """

        # Check if organisation already exist
        cur.execute("SELECT * FROM public.organizations Where org_name='%s' " % organisation)
        rows = cur.fetchall()
        if len(rows) > 0:
            cur.execute("DELETE FROM public.organizations Where org_name='%s' " % organisation)
        # Load table
        temp_org_details = gc(organisation)._getting_organisation_details()
        cur.execute("INSERT INTO public.organizations(org_name, repos, members, languages)VALUES (%s, %s, %s, %s);",
                    (organisation, int(temp_org_details["number of repositories"][0]),
                     int(temp_org_details["number of members"][0]),
                     int(temp_org_details["number of languages"][0])))
        conn.commit()

    def _load_lan_details(self, organisation):
        """ This function loads the language table in the database. """



        # Load table
        temp_lang_details = gc(organisation)._getting_languages_used()

        for index in range(len(temp_lang_details["languages"])):
            # TO-DO: Build Check
            # Check if organisation already exist
            cur.execute("SELECT * FROM public.languages WHERE org_name='%s' AND name='%s'" % (organisation, temp_lang_details["languages"][index]))
            rows = cur.fetchall()

            if len(rows) > 0:
                cur.execute("DELETE FROM public.languages WHERE org_name='%s' AND name='%s'" % (organisation, temp_lang_details["languages"][index]))

            cur.execute("INSERT INTO public.languages(name, bytes, org_name)VALUES (%s, %s, %s);",
                        (temp_lang_details["languages"][index], int(temp_lang_details["bytes"][index]), organisation))

        conn.commit()

    def _load_tables(self):
        """ This function loads both tables for organisation list. """
        for org in self.org_list:
            self._load_org_details(org)
            self._load_lan_details(org)


## Test purposes -> to be deleted
if __name__ == "__main__":
    Loader()._load_tables()
