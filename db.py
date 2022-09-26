import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres")

cur = conn.cursor()
## Testing purposes -> to be deleted
if __name__ == "__main__":
    cur.execute("SELECT * FROM public.organizations")
    rows = cur.fetchall()

    for r in rows:
        print(r)

    # cur.execute("INSERT INTO public.organizations(org_name, repos, members)VALUES (%s, %s, %s);",
    #            ("test", 143, 760))
    # cur.execute("INSERT INTO public.organizations(org_name, repos, members)VALUES (%s, %s, %s);",
    #            ("test1", 143, 760))
    # cur.execute("INSERT INTO public.organizations(org_name, repos, members)VALUES (%s, %s, %s);",
    #            ("test2", 143, 760))
    # conn.commit()

