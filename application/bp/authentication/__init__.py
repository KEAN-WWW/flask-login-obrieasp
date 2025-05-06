from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
from application.database import User, db

authentication_bp = Blueprint('authentication', __name__, template_folder='templates')

@authentication_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user is None:
            return render_template('login.html', error="User Not Found")
        if not user.check_password(password):
            return render_template('login.html', error="Password Incorrect")

        login_user(user)
        return redirect(url_for('authentication.dashboard'))

    return render_template('login.html')

@authentication_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@authentication_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage.home'))



