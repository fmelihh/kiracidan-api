from typing import Dict, Any
from sqlalchemy import Column, String, Integer

from .abstract import Mixin


class Roles(Mixin):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    role_name = Column(String(50), nullable=False, unique=True)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "role_name": self.role_name
        }
