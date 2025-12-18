from flask import Blueprint, request, jsonify, redirect
from extensions import db
from models import Content

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/content", methods=["POST"])
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