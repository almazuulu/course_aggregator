from __future__ import annotations

from datetime import datetime
from typing import List
from uuid import UUID

from models.base_model import Base
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID as SQL_UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(
        SQL_UUID(as_uuid=True),
        primary_key=True,
        default=text("uuid_generate_v4()"),
    )
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[datetime]

    courses: Mapped[List["Course"]] = relationship(  # noqa
        secondary="favorite",
        back_populates="users",
    )
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="user")  # noqa
