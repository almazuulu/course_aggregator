from __future__ import annotations

import logging
from typing import List
from uuid import UUID

from course.courses.schemas.course import CourseCreateResponseSchema
from course.courses.schemas.course import CourseCreateUpdateSchema
from course.courses.schemas.course import CourseSchema
from course.courses.services.course import CourseService
from fastapi import APIRouter
from fastapi import Depends
from starlette import status

router = APIRouter()


logger = logging.getLogger("api")


@router.get("/list/", response_model=List[CourseSchema], status_code=status.HTTP_200_OK)
async def list_courses(
    service: CourseService = Depends(),
) -> List[CourseSchema]:
    return await service.get_all()


@router.get("/{id}/", response_model=CourseSchema, status_code=status.HTTP_200_OK)
async def get_course(id: UUID, service: CourseService = Depends()) -> CourseSchema:
    course = await service.get_course(id)
    return CourseSchema.model_validate(course)


@router.post(
    "/",
    response_model=CourseCreateResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_course(
    data: CourseCreateUpdateSchema,
    service: CourseService = Depends(),
) -> CourseCreateResponseSchema:
    return await service.create_course(data)


@router.put("/{id}/", response_model=CourseSchema, status_code=status.HTTP_202_ACCEPTED)
async def update_course(
    id: UUID,
    data: CourseCreateUpdateSchema,
    service: CourseService = Depends(),
) -> CourseSchema:
    return await service.update_course(id, data)


@router.delete("/{id}/")
async def delete_course(
    id: UUID,
    service: CourseService = Depends(),
) -> None:
    await service.delete_course(id)
