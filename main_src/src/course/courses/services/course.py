from __future__ import annotations

from typing import List

from core.deps import get_session
from course.courses.repositories.course import CourseRepository
from course.courses.schemas.course import CourseSchema
from fastapi import Depends
from services.base import BaseService
from sqlalchemy.ext.asyncio import AsyncSession


class CourseService(BaseService):
    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        self.repository: CourseRepository = CourseRepository(session)

    async def get_all(self) -> List[CourseSchema]:
        return await self.repository.read_all()
