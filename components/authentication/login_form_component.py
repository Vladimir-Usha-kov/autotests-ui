from playwright.sync_api import Page
from components.base_components import BaseComponent
from elements.input import Input


class LogonFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')

    def fill(self, email: str, password: str):
        if email is not None:
            self.email_input.fill(email)
            self.email_input.check_have_value(email)
        if password is not None:
            self.password_input.fill(password)
            self.password_input.check_have_value(password)

    def check_visible(self):
        self.email_input.check_visible()
        self.password_input.check_visible()
