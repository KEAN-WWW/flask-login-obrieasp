from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'  # This defines the table name

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, email, password_hash):
        self.email = email
        self.password_hash = password_hash

    def check_password(self, password):
        return self.password_hash == password  # Simple password check for testing

    @classmethod
    def create(cls, email, password):
        return cls(email=email, password_hash=password)
