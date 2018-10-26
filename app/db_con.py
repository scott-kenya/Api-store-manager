# import psycopg2
# import pprint
# import os

# from queries import queries

# def connectdb():
#     try:
#         uri = "dbname='store2018' host='localhost' user='scott' port='5432' password='password'"

#         conn = psycopg2.connect(uri)
#         return conn
#     except(Exception, psycopg2.DatabaseError) as error:
#         print("Cannot connect to database" , error)


# def create_tables():
#     try:
#         conn = connectdb()
#         curr = conn.cursor()
#         for query in queries:
#             curr.execute(query)
#     except(Exception, psycopg2.DatabaseError) as error:
#         print("Connection Error:", error)

#     finally:
#         curr.close()
#         conn.commit()
        

        


















