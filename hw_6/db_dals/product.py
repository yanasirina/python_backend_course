from .base import BaseDal
from hw_6.db_models import Product


class ProductDal(BaseDal):
    def create_product_batch(self, product_names: list[str]) -> list[Product]:
        products = [Product(name=product_name) for product_name in product_names]
        self._session.add_all(products)
        self._session.commit()
        return products
