from flask import Flask
from app.models import db
from config import Config # Importing Config from config.py

app = Flask(__name__)
app.config.from_objects(Config)
db.init_app(app)