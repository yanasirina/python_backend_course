from sqlalchemy import Row, func

from .base import BaseDal
from hw_6.db_models import Order, User


class OrderDal(BaseDal):
    def create_order(self, user_id: int, product_id: int, quantity: int) -> Order:
        order = Order(user_id=user_id, product_id=product_id, quantity=quantity)
        self._session.add(order)
        self._session.commit()
        return order

    def get_orders_with_users(self) -> list[Row[tuple[Order, User]]]:
        orders_with_users = self._session.query(Order, User).join(User).all()
        return orders_with_users

    def get_orders_count_per_user(self) -> list[Row[tuple[User, int]]]:
        orders_count_per_user = (
            self._session.query(User, func.count(Order.id).label('order_count'))
            .join(Order)
            .group_by(User)
            .having(func.count(Order.id) > 0)
            .all()
        )
        return orders_count_per_user
