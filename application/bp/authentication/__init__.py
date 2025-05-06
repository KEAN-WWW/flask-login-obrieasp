from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from application.database import db, User
from flask_login import login_required


authentication_bp = Blueprint('authentication', __name__, template_folder='templates')

@authentication_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()  # Check if user exists
        if user is None:  # User not found
            return render_template('login.html', error="User Not Found")
        if not user.check_password(password):  # Incorrect password
            return render_template('login.html', error="Password Incorrect")

        login_user(user)  # Log the user in
        return redirect(url_for('authentication.dashboard'))  # Redirect to the dashboard page

    return render_template('login.html')



@authentication_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('homepage.html')


# Logout route
@authentication_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage.home'))  # Redirect to homepage after logout

# Home route (requires login)
@authentication_bp.route("/")
@login_required
def home():
    return render_template("homepage.html")
