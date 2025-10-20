import re
from operator import index

import allure
from playwright.sync_api import Page, expect

from components.navigation.sidebar_list_item_component import SidebarListItemComponent
from pages.base_page import BasePage


class SideBarComponents(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.logout_list_item = SidebarListItemComponent(page, 'logout')

    @allure.step('Check visible sidebar')
    def check_visible(self):
        self.dashboard_list_item.check_visible('Dashboard')
        self.courses_list_item.check_visible('Courses')
        self.logout_list_item.check_visible('Logout')

    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    @allure.step('Click courses on sidebar')
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    @allure.step('Click dashboard on sidebar')
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))