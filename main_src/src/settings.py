from functools import lru_cache
from core.base_settings import Settings


@lru_cache()
def get_settings() -> Settings:
    return Settings()