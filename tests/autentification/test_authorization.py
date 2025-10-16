import time

import allure
import pytest
from pages.autentification.login_page import LoginPage
from pages.autentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeatures
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag


@pytest.mark.authorization
@pytest.mark.regression
@allure.tag(AllureTag.AUTHORIZATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.parametrize('email, password',
                             [('user.name@gmail.com', 'password'), ('user.name@gmail.com', '  '), ('  ', 'password')])
    @allure.title('User login with wrong email or password')
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.login_component.fill(email, password)
        login_page.login_component.check_visible()
        login_page.click_button()
        login_page.check_visible_alert()

    @allure.title('User login with correct email and password')
    def test_successful_authorization(self, registration_page: RegistrationPage,
                                      login_page: LoginPage,
                                      dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user@mail.ru', username='test', password='test')
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible(username='test')
        dashboard_page.sidebar.click_logout()
        login_page.login_component.fill(email='user@mail.ru', password='test')
        login_page.click_button()
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.sidebar.check_visible()
        dashboard_page.navbar.check_visible(username='test')

    @allure.title('Navigation from login page to registration page')
    def test_navigate_from_authorization_to_registration(self,
                                                         login_page: LoginPage,
                                                         registration_page: RegistrationPage):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.click_registration_link()
        registration_page.registration_form.check_visible(email='', username='', password='')
