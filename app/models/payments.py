from typing import Dict, Any
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.sql import func
from .abstract import Mixin


class Payments(Mixin):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    target_home_id = Column(Integer, ForeignKey("home.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    type = Column(Integer, ForeignKey("payment_types.id"), nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    amount = Column(Float, nullable=False)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "target_home_id": self.target_home_id,
            "type": self.type,
            "date": self.date,
            "amount": self.amount
        }