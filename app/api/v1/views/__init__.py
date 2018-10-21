from flask import Flask, Blueprint
from flask_restful import Api, Resource
from app.api.v1.views.products import Products, Product_id
from app.api.v1.views.sales import Sales, Sale_id
from flask_jwt_extended import JWTManager
from instance.config import app_config
from flask_httpauth import HTTPBasicAuth
#from app.api.v1.views.users_view import Register, Login 

zed = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(zed)
auth = HTTPBasicAuth()

api.add_resource(Products, '/products')
api.add_resource(Product_id, '/products/<int:product_id>')
api.add_resource(Sales, '/sales')
api.add_resource(Sale_id, '/sales/<int:sale_id>')
#api.add_resource(Register, '/auth/register')
#api.add_resource(Login, '/auth/login')