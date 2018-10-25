# dbx = """
#     CREATE TABLE IF NOT EXISTS products(
#     product_id SERIAL PRIMARY KEY,
#     name VARCHAR(1000) NOT NULL,
#     price VARCHAR(255) NOT NULL,
#     quantity VARCHAR(255)
# );"""


# dby ="""CREATE TABLE IF NOT EXISTS users(
# 	user_id serial PRIMARY KEY ,
# 	fname VARCHAR(50) NOT NULL,
# 	lname VARCHAR(50),
# 	username VARCHAR(50) NOT NULL,
# 	email VARCHAR(50), 
# 	role VARCHAR(10), 
# 	date created timestamp with timezone default('now'::text)::date NOT NULL,
# 	password VARCHAR(500) not null);"""

# queries = [dbx, dby]
# 	