from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from schemas.base import OrmBaseModel


class CourseSchema(OrmBaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    category_id: int
    provider_id: UUID
    language: Optional[str] = None
    price: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime


class CourseCreateUpdateSchema(OrmBaseModel):
    title: str
    description: Optional[str] = None
    category_id: int
    provider_id: UUID
    language: Optional[str] = None
    price: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class CourseCreateResponseSchema(OrmBaseModel):
    id: UUID
    title: str
    category_id: int
    provider_id: UUID
