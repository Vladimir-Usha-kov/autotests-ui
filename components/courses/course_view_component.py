import allure
from playwright.sync_api import Page, expect

from components.base_components import BaseComponent
from components.courses.courses_view_menu_component import CoursesVewMenuComponent
from data.data import CheckVisibleCourseCardParams
from elements.image import Image
from elements.text import Text


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CoursesVewMenuComponent(page)

        # Карточка курса
        self.course_title = Text(page, 'course-widget-title-text', 'Title')
        self.course_image = Image(page, 'course-preview-image', 'Preview')
        self.course_max_score_text = Text(page, 'course-max-score-info-row-view-text', 'Max score')
        self.course_min_score_text = Text(page, 'course-min-score-info-row-view-text', 'Min score')
        self.course_estimated_time_text = Text(page, 'course-estimated-time-info-row-view-text', 'estimated-time')

    @allure.step('Check visible course card "{params.index}"')
    def check_visible_card(self, params: CheckVisibleCourseCardParams):
        self.course_image.check_visible(nth=params.index)

        self.course_title.check_visible(nth=params.index)
        self.course_title.check_have_text(params.title, nth=params.index)

        self.course_max_score_text.check_visible(nth=params.index)
        self.course_max_score_text.check_have_text(f'Max score: {params.max_score}', nth=params.index)

        self.course_min_score_text.check_visible(nth=params.index)
        self.course_min_score_text.check_have_text(f'Min score: {params.min_score}', nth=params.index)

        self.course_estimated_time_text.check_visible(nth=params.index)

        self.course_estimated_time_text.check_have_text(f'Estimated time: {params.estimated_time}',
                                                        nth=params.index)
