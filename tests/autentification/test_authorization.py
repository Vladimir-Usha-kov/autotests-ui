import time

import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.autentification.login_page import LoginPage
from pages.autentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeatures
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.routes import AppRoute


@pytest.mark.authorization
@pytest.mark.regression
@allure.tag(AllureTag.AUTHORIZATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.parametrize('email, password',
                             [('user.name@gmail.com', 'password'), ('user.name@gmail.com', '  '), ('  ', 'password')])
    @allure.title('User login with wrong email or password')
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.login_component.fill(email, password)
        login_page.login_component.check_visible()
        login_page.click_button()
        login_page.check_visible_alert()

    @allure.severity(Severity.BLOCKER)
    @allure.title('User login with correct email and password')
    def test_successful_authorization(self, registration_page: RegistrationPage,
                                      login_page: LoginPage,
                                      dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password)

        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.navbar.check_visible(username=settings.test_user.username)
        dashboard_page.sidebar.click_logout()
        login_page.login_component.fill(
            email=settings.test_user.email,
            password=settings.test_user.password
        )

        login_page.click_button()
        dashboard_page.dashboard_toolbar.check_visible()
        dashboard_page.sidebar.check_visible()
        dashboard_page.navbar.check_visible(username=settings.test_user.username)

    @allure.title('Navigation from login page to registration page')
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(self,
                                                         login_page: LoginPage,
                                                         registration_page: RegistrationPage):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()
        registration_page.registration_form.check_visible(email='', username='', password='')
