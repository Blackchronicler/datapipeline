from git_crawler import GitCrawler as gc
from db import cur, conn

org_list = ["facebook", "twitter", "netflix", "adobe", "ubuntu"]

for org in org_list:
    cur.execute("SELECT * FROM public.organizations Where org_name='%s' " % org)
    rows = cur.fetchall()
    if len(rows) > 0:
        cur.execute("DELETE FROM public.organizations Where org_name='%s' " % org)

    temp = gc(org)._getting_organisation_details()
    cur.execute("INSERT INTO public.organizations(org_name, repos, members, languages)VALUES (%s, %s, %s, %s);",
                (org, int(temp["number of repositories"][0]), int(temp["number of members"][0]),
                 int(temp["number of languages"][0])))

conn.commit()
