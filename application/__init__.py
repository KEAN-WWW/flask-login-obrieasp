from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'authentication.login'  # Redirect if not logged in

def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    from application.bp.authentication import authentication_bp
    from application.bp.homepage import homepage_bp
    app.register_blueprint(authentication_bp)
    app.register_blueprint(homepage_bp)

    with app.app_context():
        from application.database import User
        db.create_all()

    return app

# User loader must be at global level
@login_manager.user_loader
def load_user(user_id):
    from application.database import User
    return User.query.get(int(user_id))
