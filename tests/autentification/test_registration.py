import pytest
from playwright.sync_api import Page
from components.authentication.registration_form_component import RegistrationFormComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(dashboard_page: DashboardPage, registration_page: RegistrationPage, chromium_page: Page):
    registration_form_component = RegistrationFormComponent(chromium_page)
    dashboard_toolbar_view_component = DashboardToolbarViewComponent(chromium_page)

    registration_page.open("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    
    registration_form_component.check_visible(email="username@gmail.com",username="username",password="password")
    registration_page.click_registration_button()
    dashboard_toolbar_view_component.check_visible() # добавил компонент тут
