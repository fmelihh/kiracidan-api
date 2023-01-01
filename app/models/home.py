from typing import Dict, Any
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .abstract import Mixin

from .payments import Payments


class Home(Mixin):
    __tablename__ = "home"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    comment = Column(String(), nullable=True)
    address = Column(String(), nullable=False)
    status_id = Column(Integer, ForeignKey("home_status.id"), nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    tenant_id = Column(Integer, ForeignKey("user.id"), unique=True, nullable=True)
    payment_amount = Column(Integer, nullable=False)
    deposit = Column(Integer, nullable=True)
    payment_period = Column(Integer, nullable=True)
    payments = relationship("Payments", backref="payments", lazy="dynamic", foreign_keys=Payments.target_home_id)

    def to_dict(self) -> Dict[str, Any]:
        return {
           "id": self.id,
           "status_name": self.status_name
        }