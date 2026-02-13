from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from components.authentication.login_form_component import LoginFormComponent
import pytest


@pytest.mark.courses
@pytest.mark.regression
@pytest.mark.parametrize('email, password', [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])
def test_wrong_email_or_password_authorization(chromium_page: Page, login_page: LoginPage, email:str, password:str):

    login_form_component = LoginFormComponent(chromium_page)

    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_form_component.check_visible(email=email, password=password)
    login_page.click_login_button()
    login_page.check_wrong_element_alert_is_visible("Wrong email or password")