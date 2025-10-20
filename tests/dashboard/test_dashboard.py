import allure
import pytest
from allure_commons.types import Severity

from pages.dashboard.dashboard_page import DashboardPage
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeatures
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag




@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.DASHBOARD, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.suite(AllureFeatures.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
class TestDashboard:
    @allure.tag(AllureTag.DASHBOARD)
    @allure.title('Check displaying of dashboard page')
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.dashboard_toolbar.check_visible()
        dashboard_page_with_state.check_visible_students_chart()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_activities_chart()
