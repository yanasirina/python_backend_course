import logging
import random

from sqlalchemy.orm import sessionmaker

from hw_6.db_models import engine
from hw_6.db_dals import UserDal, OrderDal, ProductDal


if __name__ == '__main__':
    logger = logging.getLogger()
    Session = sessionmaker(bind=engine)
    session = Session()

    user_dal = UserDal(session=session, logger=logger)
    product_dal = ProductDal(session=session, logger=logger)
    order_dal = OrderDal(session=session, logger=logger)

    # создадим пользователя, проверим, что он появился в бд
    first_user = user_dal.create_user(name='Yana Sirina')
    first_user_from_db = user_dal.get_user_by_id(user_id=first_user.id)
    print(first_user_from_db.name)  # Yana Sirina

    # попробуем изменить имя пользователя
    user_dal.update_user_name(user_id=first_user.id, new_name='New Name')
    first_user_from_db = user_dal.get_user_by_id(user_id=first_user.id)
    print(first_user_from_db.name)  # New Name

    # получим несуществующего пользователя из бд
    not_existing_user_id = 100_000
    print(user_dal.get_user_by_id(user_id=not_existing_user_id))  # None (log: No user with id=100000)
    user_dal.update_user_name(user_id=not_existing_user_id, new_name='Not Exist')  # (log: Cannot update user with id=100000 (no such user))

    # создадим больше пользователей, проверим метода для получения всех пользователей
    user_dal.create_user(name='Ivan Petrov')
    user_dal.create_user(name='Petr Ivanov')
    user_dal.create_user(name='No Name')
    users = user_dal.get_users()
    print([user.name for user in users])  # ['New Name', 'Ivan Petrov', 'Petr Ivanov', 'No Name']

    # проверим метод удаления пользователя из бд
    was_deleted = user_dal.delete_user(user_id=first_user.id)
    print(was_deleted)  # True
    print(user_dal.get_user_by_id(user_id=first_user.id))  # None (log: No user with id=1)

    # проверим удаление несуществующего пользователя
    was_deleted = user_dal.delete_user(user_id=not_existing_user_id)
    print(was_deleted)  # False

    # попробуем создать несколько товаров за раз
    products = product_dal.create_product_batch(product_names=['Phone', 'TV', 'Laptop'])
    print([product.name for product in products])  # ['Phone', 'TV', 'Laptop']

    # сгенерируем 10 случайных заказов
    product_ids = [product.id for product in products]
    user_ids = [user.id for user in user_dal.get_users()]
    for _ in range(10):
        random_user_id = random.choice(user_ids)
        random_product_id = random.choice(product_ids)
        random_quantity = random.randint(1, 5)
        order_dal.create_order(user_id=random_user_id, product_id=random_product_id, quantity=random_quantity)

    # выведем заказы вместе с пользователями-заказчиками
    orders_with_users = order_dal.get_orders_with_users()
    print([(order.id, user.name) for order, user in orders_with_users])  # [(1, 'Petr Ivanov'), (2, 'Ivan Petrov'), (3, 'No Name'), (4, 'No Name'), (5, 'Ivan Petrov'), (6, 'Petr Ivanov'), (7, 'Ivan Petrov'), (8, 'Ivan Petrov'), (9, 'Ivan Petrov'), (10, 'Petr Ivanov')]

    # сгруппируем заказы по пользователям и посчитаем количество заказов у каждого пользователя
    orders_count_per_user = order_dal.get_orders_count_per_user()
    print([(user.name, count) for user, count in orders_count_per_user])  # [('Ivan Petrov', 5), ('Petr Ivanov', 3), ('No Name', 2)]
