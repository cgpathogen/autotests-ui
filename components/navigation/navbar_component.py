from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)


        self.title_ui_courses = self.page.get_by_test_id("navigation-navbar-app-title-text")
        self.welcome_title = self.page.get_by_test_id("navigation-navbar-welcome-title-text")


    def check_visibility(self, ui_courses_text=None, welcome_title=None):
        expect(self.title_ui_courses).to_be_visible()
        expect(self.title_ui_courses).to_have_text(ui_courses_text)

        expect(self.welcome_title).to_be_visible()
        expect(self.welcome_title).to_have_text(f"Welcome, {welcome_title}!")