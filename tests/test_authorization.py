from playwright.sync_api import Page, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
@pytest.mark.parametrize('email, password', [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])
def test_wrong_email_or_password_authorization(chromium_page: Page, email:str, password:str):

    email_input = chromium_page.get_by_test_id("login-form-email-input").locator("input")
    email_input.fill(email)

    password_input = chromium_page.get_by_test_id("login-form-password-input").locator("input")
    password_input.fill(password)

    login_button = chromium_page.get_by_test_id("login-page-login-button")
    login_button.click()

    wrong_element_alert = chromium_page.get_by_test_id("login-page-wrong-email-or-password-alert")
    expect(wrong_element_alert).to_have_text("Wrong email or password")
