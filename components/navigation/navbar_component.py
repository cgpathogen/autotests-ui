from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)


        self.title_ui_courses = Text(self.page,"navigation-navbar-app-title-text", "title-ui-course")
        self.welcome_title = Text(self.page, "navigation-navbar-welcome-title-text", "welcome-title")


    def check_visibility(self, ui_courses_text=None, welcome_title=None):
        self.title_ui_courses.check_visible()
        self.title_ui_courses.check_have_text(ui_courses_text)

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f"Welcome, {welcome_title}!")