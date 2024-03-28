from __future__ import annotations

from fastapi import HTTPException
from fastapi import status


class NotFoundException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
