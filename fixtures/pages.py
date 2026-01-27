import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.fixture(scope="function")
def registration_page(chromium_page: RegistrationPage) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)


@pytest.fixture(scope="function")
def dashboard_page(chromium_page: DashboardPage) -> DashboardPage:
    return DashboardPage(page=chromium_page)