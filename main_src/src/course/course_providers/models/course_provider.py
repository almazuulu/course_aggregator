from __future__ import annotations

from typing import List

from models.base_model import BaseCreateUpdated
from sqlalchemy import String
from sqlalchemy import UUID as SQL_UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class CourseProvider(BaseCreateUpdated):
    __tablename__ = "course_provider"

    id: Mapped[SQL_UUID] = mapped_column(SQL_UUID, primary_key=True)
    name: Mapped[str]
    description: Mapped[str] = mapped_column(String, nullable=True)
    website: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)

    courses: Mapped[List["Course"]] = relationship(  # noqa
        "Course",
        back_populates="course_providers",
    )
