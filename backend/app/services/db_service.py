from app.models import Product

def get_data(indices):
    neighbors = Product.query.filter(Product.id.in_(indices)).all()
    return neighbors