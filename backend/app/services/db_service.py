from app import db
from app.models import Product

def init_db(app):
    with app.app_context():
        db.create_all()
        print("Initialized table and created tables");