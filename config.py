import os
import secrets

class Config:
    """Default Config Settings"""
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', "TRUE") == "TRUE"  # Ensuring it's a boolean
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', "sqlite:///app.db")
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_urlsafe(16))  # Allow SECRET_KEY to be set via env
