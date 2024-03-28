from __future__ import annotations

from datetime import datetime
from typing import List
from uuid import UUID

from models.base_model import BaseCreateUpdated
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID as SQL_UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Course(BaseCreateUpdated):
    __tablename__ = "course"

    id: Mapped[UUID] = mapped_column(
        SQL_UUID(as_uuid=True),
        primary_key=True,
        default=text("uuid_generate_v4()"),
    )
    title: Mapped[str]
    description: Mapped[str] = mapped_column(String, nullable=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("course_category.id"))
    provider_id: Mapped[UUID] = mapped_column(
        SQL_UUID(as_uuid=True),
        ForeignKey("course_provider.id"),
    )
    language: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[int] = mapped_column(String, nullable=True)
    start_date: Mapped[datetime] = mapped_column(String, nullable=True)
    end_date: Mapped[datetime] = mapped_column(String, nullable=True)

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
