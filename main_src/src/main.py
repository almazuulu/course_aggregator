from __future__ import annotations

import logging
from logging.config import dictConfig

import uvicorn
from core.deps import get_settings
from course.courses.api import api as course_api
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

settings = get_settings()
dictConfig(settings.log_config)

logger = logging.getLogger("api")

app = FastAPI(
    title=settings.APP_NAME,
    description=f"{settings.OPENAPI_DESCRIPTION}",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

logger.info("App started with:")
logger.info("DEBUG=%s", settings.DEBUG)
logger.info("DB_ENGINE_POOL_PRE_PING=%s", settings.DB_ENGINE_POOL_PRE_PING)
logger.info("DB_ENGINE_POOL_RECYCLE=%s", settings.DB_ENGINE_POOL_RECYCLE)
logger.info("DB_ENGINE_POOL_SIZE=%s", settings.DB_ENGINE_POOL_SIZE)
logger.info("DB_ENGINE_MAX_OVERFLOW=%s", settings.DB_ENGINE_MAX_OVERFLOW)
logger.info("DB_ENGINE_POOL_TIMEOUT=%s", settings.DB_ENGINE_POOL_TIMEOUT)
logger.info("SQL_ENGINE_ECHO=%s", settings.SQL_ENGINE_ECHO)

app.include_router(course_api.router, prefix="/api/v1")

add_pagination(app)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
