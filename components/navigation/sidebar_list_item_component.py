from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text
from elements.button import Button
from typing import Pattern

class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(self.page, f"{identifier}-drawer-list-item-icon", "sidebar_icon")
        self.title = Text(self.page,f"{identifier}-drawer-list-item-title-text", "sidebar_title")
        self.button = Button(self.page, f"{identifier}-drawer-list-item-button", "sidebar_button")


    def check_visible(self,title_text: str):
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(title_text)

        self.button.check_visible()


    def navigate(self, url: Pattern[str]):
        self.button.click()
        self.check_url(url)