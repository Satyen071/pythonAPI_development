import json

from flask import jsonify, request
from flask import Blueprint
from app.service.product_service import *

home_bp = Blueprint('home', __name__)


@home_bp.route('/add_product', methods=['POST'])
def create_data():
    data = request.json
    product = Product(data['name'], data['in_stock'], data['quantity'], data['price'])
    print("calling create data function")
    response = add_product(product)
    return jsonify(response)


@home_bp.route('/get_all_products', methods=['GET'])
def get_all_products():
    all_product_list = get_all_product()
    return all_product_list



