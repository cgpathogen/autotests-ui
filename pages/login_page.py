from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from elements.button import Button


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = self.page.get_by_test_id("authentication-ui-course-title-text")
        self.login_button = Button(page,"login-page-login-button", "login_button")
        self.wrong_element_alert = Button(page, "login-page-wrong-email-or-password-alert", "wrong_element_alert")


    def click_login_button(self):
        self.login_button.click()


    def check_wrong_element_alert_is_visible(self, text):
        self.wrong_element_alert.check_visible()
        self.wrong_element_alert.check_have_text(text)
