from __future__ import annotations

import logging

from course.courses.api.api_v1.endpoints.courses import router as courses_router
from fastapi import APIRouter

router = APIRouter()


logger = logging.getLogger("api")


router.include_router(courses_router, prefix="/course", tags=["courses"])
