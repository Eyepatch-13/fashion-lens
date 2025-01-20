from app.extensions import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(20))
    masterCategory = db.Column(db.String(100))
    subCategory = db.Column(db.String(100))
    articleType = db.Column(db.String(100))
    baseColour = db.Column(db.String(50))
    season = db.Column(db.String(50))
    year = db.Column(db.Integer)
    usage = db.Column(db.String(50))
    productDisplayName = db.Column(db.String(255))
