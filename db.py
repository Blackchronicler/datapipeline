import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres")

cur = conn.cursor()
#print(res["organisation"])

# cur.execute("INSERT INTO public.organizations(org_name, repos, members)VALUES (%s, %s, %s);",
#            ("test", 143, 760))
# cur.execute("INSERT INTO public.organizations(org_name, repos, members)VALUES (%s, %s, %s);",
#            ("test1", 143, 760))
# cur.execute("INSERT INTO public.organizations(org_name, repos, members)VALUES (%s, %s, %s);",
#            ("test2", 143, 760))
# conn.commit()

cur.execute("SELECT * FROM public.organizations")
rows = cur.fetchall()

for r in rows:
    print(r)

