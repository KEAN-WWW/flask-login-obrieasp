from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    # Import blueprints and register them
    from application.bp.authentication import authentication_bp
    from application.bp.homepage import homepage_bp
    app.register_blueprint(authentication_bp)
    app.register_blueprint(homepage_bp)

    # Ensure the app context is set correctly
    with app.app_context():
        from application.database import User  # Import the User model
        db.create_all()  # Create all tables (including 'users')

    return app

# This is required for the login manager to load the user from the session
@login_manager.user_loader
def load_user(user_id):
    from flask_login import UserMixin
    class DummyUser(UserMixin):
        def __init__(self, id):
            self.id = id
    return DummyUser(user_id)
