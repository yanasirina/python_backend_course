from typing import Optional

import sqlalchemy.exc

from .base import BaseDal
from hw_6.db_models import User


class UserDal(BaseDal):
    def create_user(self, name: str) -> User:
        user = User(name=name)
        self._session.add(user)
        self._session.commit()
        return user

    def get_users(self) -> list[type[User]]:
        users = self._session.query(User).all()
        return users

    def get_user_by_id(self, user_id: int) -> Optional[type[User]]:
        try:
            user = self._session.query(User).filter_by(id=user_id).one()
            return user
        except sqlalchemy.exc.NoResultFound:
            self._logger.error(f'No user with id={user_id}')

    def update_user_name(self, user_id: int, new_name: str) -> type[User]:
        if user := self.get_user_by_id(user_id=user_id):
            user.name = new_name
            self._session.commit()
            return user
        else:
            self._logger.error(f'Cannot update user with id={user_id} (no such user)')

    def delete_user(self, user_id: int) -> bool:
        if user_to_delete := self.get_user_by_id(user_id=user_id):
            self._session.delete(user_to_delete)
            self._session.commit()
            was_deleted = True
        else:
            was_deleted = False
        return was_deleted

