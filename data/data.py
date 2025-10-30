from pydantic import BaseModel


class CheckVisibleCourseCardParams(BaseModel):
    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str

class CourseCardFormParams(BaseModel):
    title: str
    estimated_time: str
    description: str
    max_score: str
    min_score: str