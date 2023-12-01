from sqlalchemy.orm import Session
from logging import Logger


class BaseDal:
    def __init__(self, session: Session, logger: Logger):
        self._session = session
        self._logger = logger
