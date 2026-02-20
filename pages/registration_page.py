from pages.base_page import BasePage
from playwright.sync_api import Page

from elements.input import Input
from elements.button import Button


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page=page)

        self.user_email_input = Input(self.page, "registration-form-email-input", "user_email_input")
        self.username_input = Input(self.page, "registration-form-username-input", "username_input")
        self.password_input = Input(self.page, "registration-form-password-input", "password_input")
        self.registration_button = Button(self.page, "registration-page-registration-button", "registration-button")


    def fill_registration_form(self, email: str, username: str, password: str):
        self.user_email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.registration_button.click()


    def click_registration_button(self):
        self.registration_button.click()