from __future__ import annotations

from typing import List

from course.courses.models import Course
from course.courses.schemas.course import CourseSchema
from repositories.base import BaseRepository
from sqlalchemy import select


class CourseRepository(BaseRepository):
    async def read_all(self) -> List[CourseSchema]:
        statement = select(Course).order_by(Course.id)
        result = await self.all(statement)
        return [CourseSchema.model_validate(item) for item in result]
