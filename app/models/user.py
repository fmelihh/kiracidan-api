from typing import Dict, Any
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from .comments import Comments
from .abstract import Mixin


class User(Mixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String(100), nullable=False)
    family_name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    phone_number = Column(String(15), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), unique=True)
    role = relationship("Roles", backref=backref("role"))

    user_who_commented = relationship("Comments", backref="user_who_commented", lazy="dynamic",
                                      foreign_keys=Comments.user_who_commented_id)
    commented_user = relationship("Comments", backref="commented_user",  lazy="dynamic",
                                  foreign_keys=Comments.commented_user_id)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "family_name": self.family_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "role": self.role.role_name
        }
