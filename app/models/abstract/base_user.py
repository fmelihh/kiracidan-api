from abc import abstractmethod
from typing import Dict, Any

from app.db.postgres import Base
from sqlalchemy import Column, Integer


class Mixin(Base):
    """base abstract class inherits other orm classes"""
    __abstract__ = True
    id = Column(Integer, primary_key=True, unique=True)

    @classmethod
    @abstractmethod
    def __tablename__(cls) -> str:
        """
        Every User Table Needs a Name
        :return:
        """

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """
        Returns the attributes of each user_service table in dict form
        :return:
        """
        pass

