from __future__ import annotations

from models.base_model import Base
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class CourseCategory(Base):
    __tablename__ = "course_category"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    description: Mapped[str]

    course = relationship("Course", back_populates="course_categories")
