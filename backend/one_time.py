from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv
import os

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Products model
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(50))
    masterCategory = db.Column(db.String(100))
    subCategory = db.Column(db.String(100))
    articleType = db.Column(db.String(100))
    baseColour = db.Column(db.String(50))
    season = db.Column(db.String(50))
    year = db.Column(db.Integer)
    usage = db.Column(db.String(100))
    productDisplayName = db.Column(db.String(255))

def create_database(csv_path):
    """
    Creates the database and populates it with data from the CSV file.

    Args:
        csv_path (str): Path to the styles.csv file.
    """
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully.")

        # Read the CSV file and insert data
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            products = []
            for row in reader:
                product = Product(
                    id=int(row['id']),
                    gender=row['gender'],
                    masterCategory=row['masterCategory'],
                    subCategory=row['subCategory'],
                    articleType=row['articleType'],
                    baseColour=row['baseColour'],
                    season=row['season'],
                    year=int(row['year']),
                    usage=row['usage'],
                    productDisplayName=row['productDisplayName']
                )
                products.append(product)

            # Bulk insert the products
            db.session.bulk_save_objects(products)
            db.session.commit()
            print(f"Inserted {len(products)} rows into the database.")

if __name__ == "__main__":
    # Define the CSV path
    csv_path = os.path.join("instance", "styles.csv")
    if os.path.exists(csv_path):
        create_database(csv_path)
    else:
        print(f"CSV file not found at {csv_path}")
