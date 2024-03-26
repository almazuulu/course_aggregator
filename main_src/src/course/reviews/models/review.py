from sqlalchemy import Integer, ForeignKey, UUID as SQL_UUID, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.base_model import BaseCreateUpdated


class Review(BaseCreateUpdated):
    __tablename__ = 'review'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey('course.id'), nullable=False)
    user_id: Mapped[SQL_UUID] = mapped_column(ForeignKey('user.id'), nullable=False)
    rating: Mapped[float]
    comment: Mapped[str]

    course = relationship("Course", back_populates="reviews")
    user = relationship("User", back_populates="reviews")


