from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List
from models.base_model import Base
from sqlalchemy import UUID as SQL_UUID

class User(Base):
    __tablename__ = 'user'

    id: Mapped[SQL_UUID] = mapped_column(SQL_UUID(), primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[datetime]

    courses: Mapped[List["Course"]] = relationship(  # type: ignore # noqa
        secondary="favorite", back_populates="users"
    )
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="user")