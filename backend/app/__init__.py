from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from app.routes.ai_routes import ai_bp
from app.services.annoy_service import initialize_annoy_service

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    with app.app_context():
        initialize_annoy_service()

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(app.instance_path, "products.db")}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(ai_bp, url_prefix="/ai")

    return app