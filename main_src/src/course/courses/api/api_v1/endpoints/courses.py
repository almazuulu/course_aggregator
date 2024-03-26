from __future__ import annotations

import logging
from typing import List

from course.courses.schemas.course import CourseSchema
from course.courses.services.course import CourseService
from fastapi import APIRouter
from fastapi import Depends

router = APIRouter()


logger = logging.getLogger("api")


@router.get("/list/", response_model=List[CourseSchema])
async def list_courses(
    service: CourseService = Depends(),
) -> List[CourseSchema]:
    return await service.get_all()
