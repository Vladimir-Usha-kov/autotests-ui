import dataclasses
from dataclasses import dataclass

@dataclass
class CheckVisibleCourseCardParams:
    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str

@dataclass
class CourseCardFormParams:
    title: str
    estimated_time: str
    description: str
    max_score: str
    min_score: str