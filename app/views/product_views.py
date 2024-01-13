from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.presenter.product_presenter import create_product, get_all_products, get_product_by_id, update_product, delete_product

product_blueprint = Blueprint("product", __name__)


@product_blueprint.route('/add_product', methods=['POST'])
def handle_create_products():
    return create_product()

@product_blueprint.route('/products', methods=['GET'])
def handle_get_all_products():
    return get_all_products()

@product_blueprint.route('/products/<int:product_id>', methods=["GET"])
def handle_product_by_id(product_id):
    return get_product_by_id(product_id)


@product_blueprint.route('/products/update/<int:product_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def handle_product_product(product_id):
    try:
        data = request.json 
        if not data:
            return jsonify({"error": "No data provided for update"}), 400
        
        result = update_product(product_id, data)
        return result
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@product_blueprint.route('/products/delete/<int:product_id>', methods=['DELETE'])
def handle_delete_product(product_id):
    try:
        result = delete_product(product_id)
        return result
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500