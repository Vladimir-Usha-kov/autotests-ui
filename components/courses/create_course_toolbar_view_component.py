from playwright.sync_api import Page, expect

from components.base_components import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('create-course-toolbar-title-text')
        self.button_create_course = page.get_by_test_id('create-course-toolbar-create-course-button')

    def check_visible(self, is_disabled_button: bool = True):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Create course')

        if is_disabled_button:
            expect(self.button_create_course).to_be_disabled()

        if not is_disabled_button:
            expect(self.button_create_course).to_be_enabled()

    def click_button(self):
        self.button_create_course.click()

    def check_disabled_create_course_button(self):
        expect(self.button_create_course).to_be_disabled()

