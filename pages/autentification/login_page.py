import re

import allure

from components.authentication.login_form_component import LogonFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_component = LogonFormComponent(page)
        self.login_title = Text(page, 'authentication-ui-course-title-text', 'Course')
        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page, 'login-page-registration-link', 'Registration')
        self.wrong_email_or_password_alert = Text(page, 'login-page-wrong-email-or-password-alert',
                                                  'Wrong email or password')

    def click_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()
        self.check_url(re.compile('.*/#/auth/registration'))

    @allure.step('Check visible alert wrong email and wrong password')
    def check_visible_alert(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text('Wrong email or password')

