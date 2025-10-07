import pytest
from playwright.sync_api import sync_playwright, expect, Page
import pytest

from data.data import CheckVisibleCourseCardParams
from pages.courses_list_page import CoursesListPage
from pages.login_page import LoginPage


@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize('email, password',
                         [('user.name@gmail.com', 'password'), ('user.name@gmail.com', '  '), ('  ', 'password')])
def test_wrong_email_or_password_authorization(login_page: LoginPage,chromium_page: Page, email: str, password: str
                                               ):
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.login_component.fill(email, password)
    login_page.login_component.check_visible()
    login_page.click_button()
    login_page.check_visible_alert()

