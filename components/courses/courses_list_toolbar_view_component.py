import re

import allure
from playwright.sync_api import Page, expect

from components.base_components import BaseComponent
from elements.text import Text
from elements.button import Button


class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.courses_title = Text(page, 'courses-list-toolbar-title-text', 'Title')
        self.create_course_button = Button(page,'courses-list-toolbar-create-course-button', 'Button create')

    @allure.step('Check visible course toolbar')
    def check_visible(self):
        self.courses_title.check_visible()
        self.courses_title.check_have_text('Courses')

        self.create_course_button.check_visible()

    def click_create_course_button(self):
        self.create_course_button.click()
        self.check_current_url(re.compile(r'.*/#/courses/create'))