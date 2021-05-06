import psycopg2
conn = psycopg2.connect(dbname='northwind', user='postgres', password='admin')
cur = conn.cursor()
cur.execute("CREATE TABLE superheroes (hero_id serial PRIMARY KEY, hero_name varchar,strength int); ")
cur.commit()



