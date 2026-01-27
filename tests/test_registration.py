import pytest
from playwright.sync_api import Page
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(chromium_page: Page):
    registration_page = RegistrationPage(page=chromium_page) # иницализируем страницу регистрации
    dashboard_page = DashboardPage(page=chromium_page) # инициализируем страницу дашборда

    registration_page.open("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(
        "username@gmail.com",
        "username",
        "password"
    )
    dashboard_page.check_dashboard_title_visibility()
