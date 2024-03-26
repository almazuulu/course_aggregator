from __future__ import annotations

from models.base_model import Base
from sqlalchemy import ForeignKey
from sqlalchemy import UUID as SQL_UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Favorite(Base):
    __tablename__ = "favorite"

    user_id: Mapped[SQL_UUID] = mapped_column(
        SQL_UUID,
        ForeignKey("user.id"),
        primary_key=True,
        nullable=False,
    )
    course_id: Mapped[SQL_UUID] = mapped_column(
        SQL_UUID,
        ForeignKey("course.id"),
        primary_key=True,
        nullable=False,
    )
