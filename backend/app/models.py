from app import db

class Product(db.model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(20))
    master_category = db.Column(db.String(100))
    sub_category = db.Column(db.String(100))
    article_type = db.Column(db.String(100))
    base_colour = db.Column(db.String(50))
    season = db.Column(db.String(50))
    year = db.Column(db.Integer)
    usage = db.Column(db.String(50))
    product_display_name = db.Column(db.String(255))
    image_path = db.Column(db.String(255))
