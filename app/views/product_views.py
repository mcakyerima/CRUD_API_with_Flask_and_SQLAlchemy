from flask import Blueprint, request, jsonify
from app.presenter.product_presenter import create_product, get_all_products

product_blueprint = Blueprint("product", __name__)


@product_blueprint.route('/add_product', methods=['POST'])
def handle_create_products():
    return create_product()

@product_blueprint.route('/products', methods=['GET'])
def handle_get_all_products():
    return get_all_products()

