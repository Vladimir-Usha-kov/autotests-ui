from playwright.sync_api import sync_playwright, expect, Page
import pytest

from fixtures.pages import dashboard_page
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage
from test_successful_registration import dasboard_title


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.check_registration_button_to_be_disabled()
        registration_page.registration_form.fill('user@gmail.com', 'username', 'password')
        registration_page.check_registration_button_to_be_enabled()
        registration_page.click_registration_button()

        dashboard_page.check_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        dashboard_page.dashboard_toolbar.check_visible()
