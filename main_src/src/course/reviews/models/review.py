from __future__ import annotations

from uuid import UUID

from models.base_model import BaseCreateUpdated
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Review(BaseCreateUpdated):
    __tablename__ = "review"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"), nullable=False)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
    rating: Mapped[float]
    comment: Mapped[str] = mapped_column(String, nullable=True)

    course = relationship("Course", back_populates="reviews")
    user = relationship("User", back_populates="reviews")
