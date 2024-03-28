from __future__ import annotations

from typing import List
from uuid import UUID

from models.base_model import BaseCreateUpdated
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID as SQL_UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class CourseProvider(BaseCreateUpdated):
    __tablename__ = "course_provider"

    id: Mapped[UUID] = mapped_column(
        SQL_UUID(as_uuid=True),
        primary_key=True,
        default=text("uuid_generate_v4()"),
    )
    name: Mapped[str]
    description: Mapped[str] = mapped_column(String, nullable=True)
    website: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)

    courses: Mapped[List["Course"]] = relationship(  # noqa
        "Course",
        back_populates="course_providers",
    )
