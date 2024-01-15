# app/__init__.py
import sys
from pathlib import Path

# Adding the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from app.models.product_model import db
from app.views.product_views import product_blueprint
from app.views.user_views import user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(product_blueprint, url_prefix='/api')
    app.register_blueprint(user_blueprint, url_prefix='/api/users')
    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# app = Flask(__name__)
# app.config.from_object(Config)
# db.init_app(app)

# app.register_blueprint(product_blueprint, url_prefix='/api')

# app.cli.command("create_db")

# if __name__ == '__main__':
#     app.run(debug=True)
