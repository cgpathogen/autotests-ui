from playwright.sync_api import Page

import allure
from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.expected_title = identifier.capitalize()
        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart')


    @allure.step("Check the title of the chart")
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text(self.expected_title)

        self.chart.check_visible()