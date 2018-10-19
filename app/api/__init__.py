from flask import Flask, Blueprint
from flask_restful import Api, Resource
from app.api.v1.views.products import Products, Product_id
from app.api.v1.views.sales import Sales, Sale_id, UserRegistration, UserLogin

zed = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(zed)

api.add_resource(Products, '/products')
api.add_resource(Product_id, '/products/<int:product_id>')
api.add_resource(Sales, '/sales')
api.add_resource(Sale_id, '/sales/<int:sale_id>')
api.add_resource(UserRegistration, '/registration')
api.add_resource(UserLogin, '/login')