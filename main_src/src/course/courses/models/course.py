from __future__ import annotations

from datetime import datetime
from typing import List

from models.base_model import BaseCreateUpdated
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import UUID as SQL_UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Course(BaseCreateUpdated):
    __tablename__ = "course"

    id: Mapped[SQL_UUID] = mapped_column(SQL_UUID, primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("course_category.id"))
    provider_id: Mapped[SQL_UUID] = mapped_column(
        SQL_UUID,
        ForeignKey("course_provider.id"),
    )
    language: Mapped[str]
    price: Mapped[int]
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]

    users: Mapped[List["User"]] = relationship(  # noqa
        secondary="favorite",
        back_populates="courses",
    )
    course_categories: Mapped[List["CourseCategory"]] = relationship(  # noqa
        "CourseCategory",
        back_populates="course",
    )
    course_providers = relationship("CourseProvider", back_populates="courses")
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="course")  # noqa
