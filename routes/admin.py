from flask import Blueprint, request, jsonify, redirect
from extensions import db
from models import Content

from flask_jwt_extended import jwt_required
from auth.decorators import admin_required


admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/content", methods=["POST"])
@jwt_required()
@admin_required
def add_content():
    data = request.get_json(silent=True) or request.form
    content = Content(
        title=data["title"],
        description=data["description"],
        genre=data["genre"]
    )
    db.session.add(content)
    db.session.commit()
    return redirect("/")

@admin_bp.route("/content/<int:id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_content(id):
    content = Content.query.get_or_404(id)
    db.session.delete(content)
    db.session.commit()

    return jsonify({"message": "Content deleted"})