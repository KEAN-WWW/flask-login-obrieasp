from flask import Blueprint, render_template
from flask_login import login_required

homepage_bp = Blueprint("homepage", __name__, template_folder="templates")

@homepage_bp.route("/")
def home():
    return render_template("homepage.html")
