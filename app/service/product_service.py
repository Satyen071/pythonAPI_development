from app.base import Base, engine, session
from sqlalchemy.orm.util import object_state

from app.model.product import Product

Base.metadata.create_all(engine)


def add_product(product):
    # print(product.quantity)
    session.add(product)
    session.commit()
    state = object_state(product)
    print(state)
    return "added to the store"


def get_all_product():
    product_list = session.query(Product).all()
    return product_response_format(product_list)


def product_response_format(product):
    product_list_json_format = [{"name": p.name, "is_available": p.in_stock, "quantity": p.quantity, "price": p.price}
                                for p in product]
    return product_list_json_format
