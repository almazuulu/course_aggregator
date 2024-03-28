from __future__ import annotations

from course.course_providers import models as course_providers_models
from course.reviews import models as review_models
from models.base_model import Base
from users import models as users_models
# from course.courses import models as course_models

__all__ = (
    # *course_models.__all__,
    *review_models.__all__,
    *course_providers_models.__all__,
    *users_models.__all__,
    "Base",
)
