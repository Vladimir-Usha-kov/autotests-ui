import allure
from playwright.sync_api import Page, expect

from components.base_components import BaseComponent
from data.data import CourseCardFormParams
from elements.input import Input
from elements.textarea import TextArea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Форма создания курса
        self.title_input = Input(page, 'create-course-form-title-input',
                                 'Title')
        self.estimated_time_input = Input(page,
            'create-course-form-estimated-time-input', 'Estimated')

        self.description_textarea = TextArea(page, 'create-course-form-description-input', 'Description')
        self.max_score_input = Input(page,'create-course-form-max-score-input', 'Max Score')
        self.min_score_input = Input(page,'create-course-form-min-score-input', 'Min Score')

    @allure.step('Check course card {params.title}')
    def check_visible(self, params: CourseCardFormParams):
        self.title_input.check_visible()
        self.title_input.check_have_value(params.title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.check_have_value(params.estimated_time)

        self.description_textarea.check_visible()
        self.description_textarea.check_have_value(params.description)

        self.max_score_input.check_visible()
        self.max_score_input.check_have_value(params.max_score)

        self.min_score_input.check_visible()
        self.min_score_input.check_have_value(params.min_score)

    @allure.step('Fill form create course card and check value {params.title}')
    def fill(self, params: CourseCardFormParams):
        self.title_input.fill(params.title)
        self.title_input.check_have_value(params.title)

        self.estimated_time_input.fill(params.estimated_time)
        self.estimated_time_input.check_have_value(params.estimated_time)

        self.description_textarea.fill(params.description)
        self.description_textarea.check_have_value(params.description)

        self.max_score_input.fill(params.max_score)
        self.max_score_input.check_have_value(params.max_score)

        self.min_score_input.fill(params.min_score)
        self.min_score_input.check_have_value(params.min_score)