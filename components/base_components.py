from re import Pattern

import allure

from utils.logger import get_logger
from playwright.sync_api import Page, expect

logger = get_logger('Base Component')


class BaseComponent:
    def  __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)

    def refresh_page(self):
        step = 'Reload page'
        with allure.step(step):
            logger.info(step)
            self.page.reload()