from __future__ import annotations

from uuid import UUID

from models.base_model import Base
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as SQL_UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Favorite(Base):
    __tablename__ = "favorite"

    user_id: Mapped[UUID] = mapped_column(
        SQL_UUID,
        ForeignKey("user.id"),
        primary_key=True,
        nullable=False,
    )
    course_id: Mapped[UUID] = mapped_column(
        SQL_UUID,
        ForeignKey("course.id"),
        primary_key=True,
        nullable=False,
    )
