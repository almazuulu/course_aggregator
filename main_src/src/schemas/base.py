from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic.alias_generators import to_camel


class Pagination(BaseModel):
    """
    Base model for the pagination
    """

    limit: int
    offset: int


class DateTimePeriodFilter(BaseModel):
    """
    Base model for the dates
    """

    start: datetime | None
    end: datetime | None


class CamelCaseBaseModel(BaseModel):
    """
    Base model that serializes from camel case.
    """

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class OrmBaseModel(BaseModel):
    """
    Base model that includes from_attributes flag.
    """

    model_config = ConfigDict(from_attributes=True)
