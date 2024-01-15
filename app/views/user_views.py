# app/views/user_views.py
from flask import Blueprint, request, jsonify
from app.models import db
from app.models.user_model import User, UserSchema
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json() or request.form.to_dict()
        errors = UserSchema().validate(data)

        if errors:
            return jsonify({'errors': errors}), 400
        
        new_user = User(**data)

        db.session.add(new_user)
        db.session.commit()

        return UserSchema().jsonify(new_user), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@user_blueprint.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.json
        errors = UserSchema(only=('email', 'password')).validate(data)
        
        if errors:
            return jsonify({"errors": errors}), 400
        
        user = User.query.filter_by(email=data['email']).first()

        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500
