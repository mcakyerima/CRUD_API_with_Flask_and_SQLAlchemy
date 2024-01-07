from flask import Blueprint

main_app = Blueprint('main_app', __name__)

from app.main_app import main_app
