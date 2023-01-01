from typing import Dict, Any
from sqlalchemy import Column, String, Integer, ForeignKey
from .abstract import Mixin


class Comments(Mixin):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    user_who_commented_id = Column(Integer, ForeignKey("user.id"))
    commented_user_id = Column(Integer, ForeignKey("user.id"))
    rating = Column(Integer, nullable=False)
    user_comment = Column(String(1000), nullable=True)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "user_who_commented_id": self.user_who_commented_id,
            "commented_user_id": self.commented_user_id,
            "rating": self.rating,
            "user_comment": self.user_comment,
        }