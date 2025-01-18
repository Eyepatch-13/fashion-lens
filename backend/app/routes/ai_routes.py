from flask import Blueprint, jsonify, request, render_template
import requests
import os

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
        image = request.files['file']

        if image and image.filename:
            filepath = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(filepath)
            return jsonify({"message":"Image Uploaded Successfully", "filepath": filepath}), 200
        
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

                    return jsonify({"message": "Image downloaded successfully", "filepath": filepath}), 200
                
                return jsonify({"error":"Error downloading image from url"}), 400
            except requests.RequestException as e:
                return jsonify({"error": f"Error downloading image: {str(e)}"}), 400
            
        return jsonify({"error": "No URL provided"}), 400
    return jsonify({"error": "No url or valid file provided"}), 400