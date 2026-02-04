from socket import send_fds

from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_item = SidebarListItemComponent(page, "dashboard")
        self.courses_item = SidebarListItemComponent(page, "courses")
        self.logout_item = SidebarListItemComponent(page, "logout")


    def check_visible(self):
        self.dashboard_item.check_visible("Dashboard")
        self.courses_item.check_visible("Courses")
        self.logout_item.check_visible("Logout")


    def click_logout(self):
        self.logout_item.navigate(r".*/#/auth/login")


    def click_courses(self):
        self.courses_item.navigate(r".*/#/courses")


    def click_dashboard(self):
        self.dashboard_item.navigate(f".*/#/dashboard")