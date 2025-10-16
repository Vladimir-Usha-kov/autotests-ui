from playwright.sync_api import Page, expect
from elements.text import Text
from elements.button import Button
from components.base_components import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.button_create_course = Button(page, 'create-course-toolbar-create-course-button',
                                           'Create Course')

    def check_visible(self, is_disabled_button: bool = True):
        self.title.check_visible()
        self.title.check_have_text('Create course')

        if is_disabled_button:
            self.button_create_course.check_disabled()

        if not is_disabled_button:
            self.button_create_course.check_enabled()

    def click_button(self):
        self.button_create_course.click()

    def check_disabled_create_course_button(self):
        self.button_create_course.check_disabled()
