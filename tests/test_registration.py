import pytest
from playwright.sync_api import Page
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(dashboard_page: DashboardPage, registration_page: RegistrationPage):
    registration_page = RegistrationPage(page=dashboard_page)
    dashboard_page = DashboardPage(page=registration_page)

    registration_page.open("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(
        "username@gmail.com",
        "username",
        "password"
    )
    dashboard_page.check_dashboard_title_visibility()
