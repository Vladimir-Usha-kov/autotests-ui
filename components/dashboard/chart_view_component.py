from playwright.sync_api import Page, expect
from elements.text import Text
from elements.image import Image

from components.base_components import BaseComponent


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, char_type: str):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{char_type}-chart', 'Chart')


    def check_visible(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(title)
        self.chart.check_visible()