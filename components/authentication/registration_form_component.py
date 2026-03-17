import allure
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.user_email = Input(self.page, "registration-form-email-input", "user_email_input")
        self.user_name = Input(self.page, "registration-form-username-input", "user_name")
        self.user_password = Input(self.page,"registration-form-password-input", "user_password")


    @allure.step("Check visible registration form")
    def check_visible(self, email: str, username: str, password: str):
        self.user_email.check_visible()
        self.user_name.check_visible()
        self.user_password.check_visible()

        self.fill(email=email, username=username,password=password)

        self.user_email.check_have_value(email)
        self.user_name.check_have_value(username)
        self.user_password.check_have_value(password)


    @allure.step("Fill registration form")
    def fill(self, email: str, username: str, password: str):
        self.user_email.fill(email)
        self.user_name.fill(username)
        self.user_password.fill(password)