import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_item = SidebarListItemComponent(page, "dashboard")
        self.courses_item = SidebarListItemComponent(page, "courses")
        self.logout_item = SidebarListItemComponent(page, "logout")


    @allure.step("Check visible sidebar")
    def check_visible(self):
        self.dashboard_item.check_visible("Dashboard")
        self.courses_item.check_visible("Courses")
        self.logout_item.check_visible("Logout")


    @allure.step("Click logout on sidebar")
    def click_logout(self):
        self.logout_item.navigate(r".*/#/auth/login")


    @allure.step("Click courses on sidebar")
    def click_courses(self):
        self.courses_item.navigate(r".*/#/courses")


    @allure.step("Click dashboard on sidebar")
    def click_dashboard(self):
        self.dashboard_item.navigate(f".*/#/dashboard")