from __future__ import annotations

from typing import List
from uuid import UUID

from commons.exceptions import NotFoundException
from core.deps import get_session
from course.courses.models import Course
from course.courses.repositories.course import CourseRepository
from course.courses.schemas.course import CourseCreateResponseSchema
from course.courses.schemas.course import CourseCreateUpdateSchema
from course.courses.schemas.course import CourseSchema
from fastapi import Depends
from services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession


class CourseService(BaseService):
    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        self.repository: CourseRepository = CourseRepository(session)

    async def get_all(self) -> List[CourseSchema]:
        return await self.repository.read_all()

    async def get_course(self, id: UUID) -> Course:
        course = await self.repository.get_course(id)
        if not course:
            raise NotFoundException(detail="Course not found!")
        return course

    async def create_course(
        self,
        data: CourseCreateUpdateSchema,
    ) -> CourseCreateResponseSchema:
        course = await self.repository.create_course(data)
        return CourseCreateResponseSchema.model_validate(course)

    async def update_course(
        self,
        id: UUID,
        data: CourseCreateUpdateSchema,
    ) -> CourseSchema:
        course = await self.get_course(id)

        course.title = data.title
        course.description = data.description
        course.category_id = data.category_id
        course.provider_id = data.provider_id
        course.language = data.language
        course.price = data.price
        course.start_date = data.start_date
        course.end_date = data.end_date

        await self.repository.update_course(course)
        return CourseSchema.model_validate(course)

    async def delete_course(self, id: UUID) -> None:
        course = await self.get_course(id)
        await self.repository.delete_course(course)
