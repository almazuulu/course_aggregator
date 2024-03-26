import os

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class APISettings(BaseSettings):
    APP_NAME: str = 'Couser Aggregator'
    OPENAPI_DESCRIPTION: str = "Сервис для агрегации курсов"
    ADMIN_EMAIL: str


class DBSettings(BaseSettings):
    DB_ENGINE_POOL_PRE_PING: bool = True
    DB_ENGINE_POOL_RECYCLE: int = -1
    DB_ENGINE_POOL_SIZE: int = 5
    DB_ENGINE_MAX_OVERFLOW: int = 10
    DB_ENGINE_POOL_TIMEOUT: int = 30
    SQL_ENGINE_ECHO: bool = False
    DATABASE_URL: str
    COURSE_AGGREGATOR_DB_CREDENTIALS: SecretStr


class Settings(APISettings, DBSettings):
    DEBUG: bool = False
    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")
    # CORS
    CORS_ALLOW_METHODS: list[str] = ["*"]
    CORS_ALLOW_ORIGINS: list[str] = (
        ["*"]
        if DEBUG
        else [
            "http://localhost:8000",
            "http://127.0.0.1:8000",
            "http://0.0.0.0:8000",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://0.0.0.0:3000",
        ]
    )
    CORS_ALLOW_HEADERS: list[str] = ["*"]

    # logger
    log_config: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "%(levelprefix)s %(asctime)s %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "use_colors": False,
            },
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": '%(levelprefix)s %(asctime)s :: %(client_addr)s - "%(request_line)s" %(status_code)s',
                "use_colors": False,
            },
        },
        "handlers": {
            "default": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
            "access": {
                "formatter": "access",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "api": {"handlers": ["default"], "level": "DEBUG"},
            "uvicorn.access": {
                "handlers": ["access"],
                "level": "INFO",
                "propagate": False,
            },
        },
    }

    @property
    def db_url(self) -> str:
        return self.DATABASE_URL % self.COURSE_AGGREGATOR_DB_CREDENTIALS.get_secret_value()

