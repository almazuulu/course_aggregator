from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import UUID as SQL_UUID
from models.base_model import Base


class Favorite(Base):
    __tablename__ = 'favorite'

    user_id: Mapped[SQL_UUID] = mapped_column(SQL_UUID, ForeignKey('user.id'), primary_key=True, nullable=False)
    course_id: Mapped[SQL_UUID] = mapped_column(SQL_UUID, ForeignKey('course.id'), primary_key=True, nullable=False)
