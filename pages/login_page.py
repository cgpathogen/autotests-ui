from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = self.page.get_by_test_id("authentication-ui-course-title-text")
        self.login_button = self.page.get_by_test_id("login-page-login-button")
        self.wrong_element_alert = self.page.get_by_test_id("login-page-wrong-email-or-password-alert")


    def click_login_button(self):
        self.login_button.click()


    def check_wrong_element_alert_is_visible(self, text):
        expect(self.wrong_element_alert).to_be_visible()
        expect(self.wrong_element_alert).to_have_text(text)
