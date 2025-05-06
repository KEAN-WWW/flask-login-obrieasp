from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from application import db  # get the already-initialized db from app

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def check_password(self, password):
        return self.password_hash == password  # simple check

    @classmethod
    def create(cls, email, password):
        return cls(email=email, password_hash=password)
