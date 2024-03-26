from __future__ import annotations

from typing import List

from models.base_model import BaseCreateUpdated
from sqlalchemy import UUID as SQL_UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class CourseProvider(BaseCreateUpdated):
    __tablename__ = "course_provider"

    id: Mapped[SQL_UUID] = mapped_column(SQL_UUID, primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    website: Mapped[str]
    address: Mapped[str]
    phone: Mapped[str]

    courses: Mapped[List["Course"]] = relationship(  # noqa
        "Course",
        back_populates="course_provider",
    )
