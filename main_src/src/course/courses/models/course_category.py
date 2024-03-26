from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.base_model import Base


class CourseCategory(Base):
    __tablename__ = 'course_category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    description: Mapped[str]

    course = relationship("Course", back_populates="course_categories")