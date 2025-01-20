from flask import send_from_directory, Blueprint, current_app
import os

db_bp = Blueprint('db', __name__)

@db_bp.route("/images/<path:filename>", methods=["GET"])
def serve_image(filename: str):
    with current_app.app_context():
        directory = os.path.join(current_app.instance_path, "images")
        return send_from_directory(directory, filename)
