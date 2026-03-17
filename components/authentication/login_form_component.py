from playwright.sync_api import  Page
from components.base_component import BaseComponent
import allure

from elements.input import Input

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = Input(self.page, "login-form-email-input","email")
        self.password_input = Input(self.page, "login-form-password-input","password")


    @allure.step("Check visible login form")
    def check_visible(self):
        self.email_input.check_visible()
        self.password_input.check_visible()


    @allure.step("Fill login form")
    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

