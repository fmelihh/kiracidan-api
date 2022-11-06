from typing import Dict, Any
from sqlalchemy import Column, Integer, String
from .abstract import Mixin


class PaymentTypes(Mixin):
    __tablename__ = "payment_types"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    payment_type = Column(String(50), nullable=False, unique=True)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "payment_type": self.payment_type
        }
