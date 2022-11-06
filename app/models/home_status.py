from typing import Dict, Any
from sqlalchemy import Column, Integer, String
from .abstract import Mixin


class HomeStatus(Mixin):
    __tablename__ = "home_status"
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    status_name = Column(String(), unique=True)

    def to_dict(self) -> Dict[str, Any]:
        return {
           "id": self.id,
           "status_name": self.status_name
        }

