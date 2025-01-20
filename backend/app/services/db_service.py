from app.models import Product
from app.utils.ai_utils import get_id_from_fullpath

def get_data(filenames):
    indices = [get_id_from_fullpath(fullpath) for fullpath in filenames]
    neighbors = Product.query.filter(Product.id.in_(indices)).all()
    return neighbors