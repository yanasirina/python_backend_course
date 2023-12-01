from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
engine = create_engine('sqlite:///sqlite.db')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    orders = relationship("Order", back_populates="user")

    def __str__(self):
        return self.name


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")

    def __str__(self):
        return f'{self.product}: {self.quantity} items'


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    orders = relationship("Order", back_populates="product")

    def __str__(self):
        return self.name


if __name__ == '__main__':
    # создадим таблицы в бд
    Base.metadata.create_all(engine)
