from typing import List
from pydantic import BaseModel


class Course(BaseModel):
    id: int
    preview_url: str
    title: str
    description: str
    progress: float
    is_active: bool



CourseList = List[Course]
