# from app.db_con import connectdb



# class Products():
# 	def save(self, name, price, quantity):
		
# 		payload = {
# 			'name': name,
# 			'price': price,
# 			'quantity': quantity
# 		}

# 		query ="""INSERT INTO products(name, price, quantity)VALUES
# 				(%(name)s, %(price)s, %(quantity)s)"""

# 		curr = connectdb.cursor()
# 		curr.execute(query, payload)
# 		connectdb.commit()
# 		return payload 

# 	def getproducts(self):
# 		dbconn = connectdb
# 		curr = connectdb.cursor()
# 		curr.execute("""SELECT product_id, name, price, quantity FROM products;""")
# 		data = curr.fetchall()
# 		resp = []

# 		for i, items in enumerator(data):
# 			product_id, name, price, quantity = items
# 			datar = dict(
# 					product_id = int(product_id), 
# 					name = name,
# 					price = int(price),
# 					quantity = int(quantity)
# 				)
# 			resp.append(datar)
# 		return resp