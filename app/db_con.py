import psycopg2
import os

url ="dbname='', host='',port='', user='', password=''"

db_url=os.getenv('DATABASE_URL')

#Initialize db to take in a url once and for all
def init_db():
	con = connection(url)
	return con

def create_tables():
	conn = connection(url)
	curr = conn.cursor()
	queries = tables()

	for query in queries:
		curr.execute(queries)
	conn.commit()


def tables():
	dbx"""Create table if not exist products(
	product_id serial PRIMARY KEY NOT NULL,
	name character varying(1000) NOT NULL,
	price numeric NOT NULL,
	quantity numeric NOT NULL,
	date created timestamp with timezone default('now'::text)::date NOT NULL)
	"""

	dby"""Create table if not exist saless(
	sale_id serial PRIMARY KEY NOT NULL,
	items character varying(200) NOT NULL,
	price numeric NOT NULL,
	attendant character varying(200) NOT NULL,
	date created timestamp with timezone default('now'::text)::date NOT NULL)
	"""

	dbz"""Create table if not exist users(
	user_id serial PRIMARY KEY NOT NULL,
	fname character varying(50) NOT NULL,
	lname character varying(50),
	username character varying(50) NOT NULL,
	email character varying(50), 
	role character varying(10), 
	date created timestamp with timezone default('now'::text)::date NOT NULL,
	password character varying(500) not null)
	"""