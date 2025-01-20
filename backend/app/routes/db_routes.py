from flask import send_from_directory, Blueprint, current_app, request, jsonify
from app.models import Product
from app.serializers.product_serializer import serialize_product, serialize_products
import os

db_bp = Blueprint('db', __name__)

@db_bp.route("/images/<path:filename>", methods=["GET"])
def serve_image(filename: str):
    with current_app.app_context():
        directory = os.path.join(current_app.instance_path, "images")
        return send_from_directory(directory, filename)
    
@db_bp.route("/products", methods=["GET"])
def get_products():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    offset = (page - 1) * limit

    products = Product.query.offset(offset).limit(10).all()
    total_items = Product.query.count()
    response = {
        "products": serialize_products(products),
        "pagination": {
            "page": page,
            "limit": limit,
            "total_items": total_items,
            "total_pages": (total_items + limit - 1) // limit
        }
    }

    return jsonify(response)

@db_bp.route("/products/<int:id>", methods=["GET"])
def get_product(id: int):
    product = Product.query.filter(Product.id==id).first()
    response = {
        "product": serialize_product(product)
    }

    return jsonify(response)