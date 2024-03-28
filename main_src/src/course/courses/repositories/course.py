from __future__ import annotations

from typing import List
from typing import Optional
from uuid import UUID

from course.courses.models import Course
from course.courses.schemas.course import CourseCreateUpdateSchema
from course.courses.schemas.course import CourseSchema
from repositories.base import BaseRepository
from sqlalchemy import select


class CourseRepository(BaseRepository):
    async def read_all(self) -> List[CourseSchema]:
        statement = select(Course).order_by(Course.id)
        result = await self.all(statement)
        return [CourseSchema.model_validate(item) for item in result]

    async def get_course(self, id: UUID) -> Optional[Course]:
        statement = select(Course).where(Course.id == id)
        return await self.one_or_none(statement)

    async def create_course(self, data: CourseCreateUpdateSchema) -> Course:
        course = Course(**data.dict())
        return await self.save(course)

    async def update_course(self, course: Course) -> Course:
        return await self.save(course)

    async def delete_course(self, course: Course) -> None:
        await self.remove(course)
