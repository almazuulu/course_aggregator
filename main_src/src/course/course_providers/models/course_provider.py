from typing import List

from sqlalchemy import UUID as SQL_UUID
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.base_model import BaseCreateUpdated


class CourseProvider(BaseCreateUpdated):
    __tablename__ = 'course_provider'

    id: Mapped[SQL_UUID] = mapped_column(SQL_UUID, primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    website: Mapped[str]
    address: Mapped[str]
    phone: Mapped[str]

    courses: Mapped[List["Course"]] = relationship("Course", back_populates="course_provider")
