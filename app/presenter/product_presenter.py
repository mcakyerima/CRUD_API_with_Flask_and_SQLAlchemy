from flask import request, jsonify
from app.models.product_model import Product, db, product_schema, products_schema

def create_product():
    try:
        name = request.json.get('name')
        description = request.json.get('description')
        price = request.json.get('price')
        qty = request.json.get('qty')

        if not name or not description or not price or not qty:
            return jsonify({"error": "Incomplete product details"}), 400

        new_product = Product(name=name, description=description, price=price, qty=qty)

        db.session.add(new_product)
        db.session.commit()

        return product_schema.jsonify(new_product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_all_products():
    """Fetches all products in the database"""
    try:
        all_products = Product.query.all()
        return products_schema.jsonify(all_products)
    except Exception as e:
        return jsonify({'error': str(e)}), 500