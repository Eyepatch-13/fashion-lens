from flask import Flask
from app.extensions import db
import os
from app.routes.ai_routes import ai_bp
from app.routes.db_routes import db_bp
from app.services.annoy_service import initialize_annoy_service

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    initialize_annoy_service(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(app.instance_path, "products.db")}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(ai_bp)
    app.register_blueprint(db_bp)

    return app