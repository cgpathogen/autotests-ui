from playwright.sync_api import expect, Page
from components.base_component import BaseComponent

from elements.input import Input

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = Input(self.page, "login-form-email-input","email")
        self.password_input = Input(self.page, "login-form-password-input","password")


    def check_visible(self, email: str, password: str):
        self.email_input.check_visible()
        self.password_input.check_visible()

        self.fill(email=email, password=password)

        self.email_input.check_have_value(email)
        self.password_input.check_have_value(password)


    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

