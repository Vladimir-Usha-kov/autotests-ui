import allure
from playwright.sync_api import Locator, expect
from ui_coverage_tool import ActionType

from utils.logger import get_logger
from elements.base_element import BaseElement

logger = get_logger('Text area')

class TextArea(BaseElement):
    @property
    def type_of(self) -> str:
        return 'text area'

    def get_locator(self, nth: int=0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('textarea').first


    def get_raw_locator(self, nth: int=0, **kwargs) -> str:
        return f'{super().get_raw_locator(nth, **kwargs)}//textarea[1]'

    def fill(self, value: str, nth: int=0, **kwargs):
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

        self.track_coverage(ActionType.FILL, nth, **kwargs)

    def check_have_value(self, value: str, nth: int=0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has value "{value}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)

        self.track_coverage(ActionType.VALUE, nth, **kwargs)