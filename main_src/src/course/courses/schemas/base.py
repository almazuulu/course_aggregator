from __future__ import annotations

from pydantic import BaseModel


class Pagination(BaseModel):
    limit: int
    offset: int
