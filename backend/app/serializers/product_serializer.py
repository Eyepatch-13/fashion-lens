from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import Product

mm = Marshmallow()

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

product_schema = ProductSchema()

def serialize_product(product):
    return product_schema.dump(product)

def serialize_products(products):
    return product_schema.dump(products, many=True)