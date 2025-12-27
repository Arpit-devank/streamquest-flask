from flask import Blueprint, request, jsonify, redirect
from extensions import db
from models import User
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(silent=True) or request.form
    user = User(
        name=data["name"],
        email=data["email"],
        password=generate_password_hash(data["password"]) # storing a hashed password for securing
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

    # return redirect("/login")


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or request.form

    email = data["email"]
    password = data["password"]

    # correct query: filter only by email
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"is_admin": user.is_admin}
        )

        return jsonify({
            "access_token": access_token,
            "is_admin": user.is_admin
        }), 200

    return jsonify({"message": "Invalid credentials"}), 401
