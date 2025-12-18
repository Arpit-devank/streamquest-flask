from flask import Blueprint, request, jsonify, redirect
from extensions import db
from models import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(silent=True) or request.form
    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"]
    )
    db.session.add(user)
    db.session.commit()
    # return jsonify({"message": "User created"}), 201

    return redirect("/login")

from flask import session

@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email, password=password).first()

    if user:
        session["user_id"] = user.id
        session["is_admin"] = user.is_admin
        return redirect("/")
    return redirect("/login")
