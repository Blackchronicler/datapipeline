from git_crawler import GitCrawler as gc
from db import cur, conn

org_list = ["facebook", "twitter", "netflix", "adobe", "ubuntu"]


class Loader:

    def __init__(self) -> None:
        print(f"Data from {org_list[:]} are loading.")

    def _load_org_details(self, organisation):
        cur.execute("SELECT * FROM public.organizations Where org_name='%s' " % organisation)
        rows = cur.fetchall()
        if len(rows) > 0:
            cur.execute("DELETE FROM public.organizations Where org_name='%s' " % organisation)

        temp_org_details = gc(organisation)._getting_organisation_details()
        cur.execute("INSERT INTO public.organizations(org_name, repos, members, languages)VALUES (%s, %s, %s, %s);",
                    (organisation, int(temp_org_details["number of repositories"][0]),
                     int(temp_org_details["number of members"][0]),
                     int(temp_org_details["number of languages"][0])))

    def _load_lan_details(self, organisation):
        temp_lang_details = gc(organisation)._getting_languages_used()

        for index in range(len(temp_lang_details["languages"])):
            cur.execute("INSERT INTO public.languages(name, bytes)VALUES (%s, %s);",
                        (temp_lang_details["languages"][index], int(temp_lang_details["bytes"][index])))


if __name__ == "__main__":
    for org in org_list:
        Loader()._load_org_details(org)
        Loader()._load_lan_details(org)

    conn.commit()
