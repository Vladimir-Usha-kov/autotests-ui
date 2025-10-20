import allure
import pytest
from allure_commons.types import Severity

from fixtures.pages import dashboard_page
from pages.dashboard.dashboard_page import DashboardPage
from pages.autentification.registration_page import RegistrationPage
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeatures
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.suite(AllureFeatures.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
class TestRegistration:
        @allure.title('Registration with correct email, username and password')
        @allure.severity(Severity.CRITICAL)
        def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
                registration_page.visit(
                        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
                registration_page.check_registration_button_to_be_disabled()
                registration_page.registration_form.fill('user@gmail.com', 'username', 'password')
                registration_page.check_registration_button_to_be_enabled()
                registration_page.click_registration_button()

                dashboard_page.dashboard_toolbar.check_visible()