from flask import request, jsonify
from app.models import db, ma
from app.models.product_model import Product, db, product_schema, products_schema



def create_product():
    try:
        data = request.json
        errors = product_schema.validate(data)

        if errors:
            return jsonify({"error": errors}), 400

        new_product = Product(**data)

        db.session.add(new_product)
        db.session.commit()

        return product_schema.jsonify(new_product), 201
    except ma.ValidationError as e:
        return jsonify({"error": e.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_all_products():
    """Fetches all products in the database"""
    try:
        all_products = Product.query.all()
        if not all_products:
            return jsonify({"error": "No products found"}), 500
        return products_schema.jsonify(all_products)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def  get_product_by_id(product_id):
    try:
        if not product_id:
            return jsonify({"error": "Provide product id"}), 400
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        else:
            return jsonify({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'qty': product.qty
            }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def update_product(product_id, data):
    try:
        if not product_id:
            return jsonify({"error": "Provide product id for update"}), 400
        
        product = Product.query.get(product_id)

        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        # update product attributes based on the provided data
        if isinstance(data, dict):
            # Handle single parameter update
            for key, value in data.items():
                setattr(product, key, value)
        elif isinstance(data, list):
            # Handle multiple parameter update
            for item in data:
                for key, value in item.items():
                    setattr(product, key, value)

        db.session.commit()

        return product_schema.jsonify(product)
    
    except Exception as e:
        return {"error": str(e)}, 500

def delete_product(product_id):
    """
    Deletes a product based on the provided product_id.

    Args:
        product_id (int): The ID of the product to be deleted.

    Returns:
        dict: A dictionary containing a message indicating the success of the deletion or an error message.
    """
    try:

        if not product_id:
            return jsonify({"error": "Provide product id for deletion"}), 400
          
        product = Product.query.get(product_id)

        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        db.session.delete(product)
        db.session.commit()

        return jsonify({"message": "Product deleted successfully"}), 200
    
    except Exception as e:
        return jsonify({"error":str(e)}), 500
