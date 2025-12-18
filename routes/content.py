from flask import Blueprint, jsonify, render_template
from models import Content

content_bp = Blueprint("content", __name__)

@content_bp.route("/contents", methods=["GET"])
def get_contents():
    contents = Content.query.all()
    result = []

    for c in contents:
        result.append({
            "id": c.id,
            "title": c.title,
            "genre": c.genre
        })

    return jsonify(result)


@content_bp.route("/", methods=["GET"])
def home():
    contents = Content.query.all()
    return render_template("index.html", contents=contents)

@content_bp.route("/details/<int:content_id>")
def details(content_id):
    item = Content.query.get_or_404(content_id)
    return render_template("details.html", item=item)


