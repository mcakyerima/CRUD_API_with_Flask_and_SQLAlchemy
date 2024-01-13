from app.models import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """A user class that defines the user table using SQLQlchemy"""
    id = db.Column(db.Intger, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    # define a setter for password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Password checker
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Class for modelling schema usign Marshmallow 
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email')