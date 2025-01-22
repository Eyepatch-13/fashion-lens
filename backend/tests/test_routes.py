import pytest
from app import create_app, db
from app.models import Product


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URL"] = 'sqlite:///:memory:'
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_db(app):
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

def test_products(client, init_db):
    init_db.session.add(Product())
    init_db.session.commit()
    response = client.get("/products")
    assert response.status_code == 200
    assert b'pagination' in response.data
    assert b'products' in response.data
    assert b'gender' in response.data

def test_products_id(client, init_db):
    init_db.session.add(Product(id=1))
    init_db.session.commit()
    response = client.get("/products/1")
    assert response.status_code == 200
    assert b'product' in response.data
    assert b'1' in response.data


def test_create_product(init_db):
    product = Product(id=99999, gender="Men", masterCategory="Footwear", subCategory="Shoes", articleType='cloth', baseColour="white",
                      season='summer', year=2222, usage='ethnic', productDisplayName="test")
    init_db.session.add(product)
    init_db.session.commit()

    product_in_db = Product.query.filter_by(id=99999).first()
    assert product_in_db is not None
    assert product_in_db.productDisplayName=="test"
    assert product_in_db.year == 2222

def test_delete_product(init_db):
    product = Product(id=99999, gender="Men", masterCategory="Footwear", subCategory="Shoes", articleType='cloth', baseColour="white",season='summer', year=2222, usage='ethnic', productDisplayName="test")
    init_db.session.add(product)
    init_db.session.commit()

    product_in_db = Product.query.filter_by(id=99999).first()
    assert product_in_db is not None

    init_db.session.delete(product_in_db)
    init_db.session.commit()

    product_in_db = Product.query.filter_by(id=99999).first()
    assert product_in_db is None

def test_update_product(init_db):
    product = Product(id=99999, gender="Men", masterCategory="Footwear", subCategory="Shoes", articleType='cloth', baseColour="white",season='summer', year=2222, usage='ethnic', productDisplayName="test")
    init_db.session.add(product)
    init_db.session.commit()

    product_in_db = Product.query.filter_by(id=99999).first()
    assert product_in_db is not None
    assert product_in_db.gender=='Men'

    product_in_db.gender="Women"
    init_db.session.commit()
    product_in_db = Product.query.filter_by(id=99999).first()
    assert product_in_db.gender=="Women"

def test_query_all(init_db):
    product1 = Product(id=99999, gender="Men", masterCategory="Footwear", subCategory="Shoes", articleType='cloth', baseColour="white",season='summer', year=2222, usage='ethnic', productDisplayName="test")
    product2 = Product(id=99998, gender="Men", masterCategory="Footwear", subCategory="Shoes", articleType='cloth', baseColour="white",season='summer', year=2222, usage='ethnic', productDisplayName="test")
    init_db.session.add(product1)
    init_db.session.add(product2)
    init_db.session.commit()

    products = Product.query.all()
    assert len(products) == 2
    assert products[0].id == 99998
    assert products[1].id == 99999
