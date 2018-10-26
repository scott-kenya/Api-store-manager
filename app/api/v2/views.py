# from flask_restful import Resource
# from flask import jsonify, make_response, request
# import psycopg2
# from models import Products


# class ProductsViews(Resource, Products):
#     def get(self):
#         query = Products().getproducts()
#         conn = connectdb()
#         curr = conn.cursor()
#         curr.execute(query)
#         rows = curr.fetchall()
#         if not rows:
#             return make_response(jsonify({
#                 'message': 'No productsfound'
#             }), 200)
#         return make_response(jsonify({
#             "Products": rows
#         }), 200)
       
#     def post(self):
#         try:
#             query = Products().addproducts(data)

#             conn = connectdb()
#             curr = conn.cursor()
#             curr.execute(query)
#             curr.close()
#             conn.commit()
#             add_res = """ Product {} added"""
#             return make_response(jsonify({
#                 'message': 'Product has been added'
#             }), 201)

#         except psycopg2.ProgrammingError:
#         	return  make_response(jsonify({
#         			'Syntax Error': 'Invalid input'
#         		}), 200)
