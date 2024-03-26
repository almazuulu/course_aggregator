from __future__ import annotations

from models.base_model import BaseCreateUpdated
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import UUID as SQL_UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Review(BaseCreateUpdated):
    __tablename__ = "review"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"), nullable=False)
    user_id: Mapped[SQL_UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
    rating: Mapped[float]
    comment: Mapped[str]

    course = relationship("Course", back_populates="reviews")
    user = relationship("User", back_populates="reviews")
