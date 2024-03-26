import uuid
from asyncio import shield
from functools import lru_cache
from logging import Logger
from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from sqlalchemy.exc import DBAPIError

from core.db_settings import create_async_session
from course.courses.schemas.base import Pagination
from config import Settings


import logging
from logging import Logger

def get_logger() -> Logger:
    return logging.getLogger("api")

@lru_cache
def get_settings() -> Settings:
    return Settings()

async def get_pagination(limit: int = 10, offset: int = 0) -> Pagination:
    return Pagination(limit=limit, offset=offset)

async def get_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    session = create_async_session()
    yield session
    await session.commit()
    await shield(session.close())