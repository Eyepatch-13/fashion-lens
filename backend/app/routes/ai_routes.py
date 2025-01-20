from flask import Blueprint, jsonify, request, render_template
import requests
import os
from app.services.search_service import get_indices
from app.services.db_service import get_data
from app.serializers.product_serializer import serialize_products
import logging

logger = logging.getLogger(__name__)

ai_bp = Blueprint('ai', __name__)

UPLOAD_FOLDER = "instance/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@ai_bp.route("/", methods=["GET"])
def index():
    """
    Returns the landing page for the site
    """
    return render_template("index.html")

@ai_bp.route("/upload", methods=["POST"])
def upload_image():
    """
    
    """
    if 'file' in request.files:
        try:
            image = request.files['file']

            if image and image.filename:
                filepath = os.path.join(UPLOAD_FOLDER, image.filename)
                image.save(filepath)
        except Exception as e:
            return jsonify({'error': 'No valid file uploaded'}), 400
    
    elif request.is_json:
        data = request.get_json()
        if 'url' in data:
            image_url = data['url']
            try:
                response = requests.get(image_url, stream=True)
                if response.status_code == 200:
                    filename = os.path.basename(image_url)
                    filepath = os.path.join(UPLOAD_FOLDER, filename)

                    with open(filepath, 'wb') as file:
                        file.write(response.content)
                else:
                    return jsonify({"error":"Error downloading image from url"}), 400
            except requests.RequestException as e:
                return jsonify({"error": f"Error downloading image: {str(e)}"}), 400
        else:  
            return jsonify({"error": "No URL provided"}), 400
    else:
        return jsonify({"error": "No url or valid file provided"}), 400

    neighbors = get_indices(filepath)
    data = get_data(neighbors)
    serialized_data = serialize_products(data)
    return jsonify({"message": serialized_data}), 200