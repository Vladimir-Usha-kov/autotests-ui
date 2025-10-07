from playwright.sync_api import Page, expect

from components.base_components import BaseComponent


class LogonFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')

    def fill(self, email: str, password: str):
        if email is not None:
            self.email_input.fill(email)
            expect(self.email_input).to_have_value(email)
        if email is not None:
            self.password_input.fill(password)
            expect(self.password_input).to_have_value(password)

    def check_visible(self):
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()