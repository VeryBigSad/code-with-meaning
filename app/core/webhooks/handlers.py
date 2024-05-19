import logging

from core.db.models import Course
from core.redis import delete_by_key, get_by_key
from core.webhooks.models import CourseList
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["v1"])
logger = logging.getLogger(__name__)


@router.get("/courses", response_model=CourseList)
async def get_courses():
    courses = await Course.filter(is_active=True)
    return courses

