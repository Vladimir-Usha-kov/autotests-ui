from playwright.sync_api import Page, expect

from components.base_components import BaseComponent
from components.courses.courses_view_menu_component import CoursesVewMenuComponent
from data.data import CheckVisibleCourseCardParams


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CoursesVewMenuComponent(page)

        # Карточка курса
        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

    def check_visible_card(self, params: CheckVisibleCourseCardParams):
        expect(self.course_image.nth(params.index)).to_be_visible()

        expect(self.course_title.nth(params.index)).to_be_visible()
        expect(self.course_title.nth(params.index)).to_have_text(params.title)

        expect(self.course_max_score_text.nth(params.index)).to_be_visible()
        expect(self.course_max_score_text.nth(params.index)).to_have_text(f'Max score: {params.max_score}')

        expect(self.course_min_score_text.nth(params.index)).to_be_visible()
        expect(self.course_min_score_text.nth(params.index)).to_have_text(f'Min score: {params.min_score}')

        expect(self.course_estimated_time_text.nth(params.index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(params.index)).to_have_text(
            f'Estimated time: {params.estimated_time}')