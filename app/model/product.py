from sqlalchemy import Column, Integer, String, Boolean, Numeric

from app.base import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(32))
    in_stock = Column('in_stock', Boolean)
    quantity = Column('quantity', Integer)
    price = Column('price', Integer)

    def __init__(self, name, in_stock, quantity, price):
        self.name = name
        self.in_stock = in_stock
        self.quantity = quantity
        self.price = price
