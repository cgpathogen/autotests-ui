import pytest
from playwright.sync_api import Playwright, Page
from pages.registration_page import RegistrationPage
from config import settings
from tools.routes import AppRoute

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.open(AppRoute.REGISTRATION)
    registration_page.fill_registration_form(
        email=settings.test_user.email,
        password=settings.test_user.password,
        username=settings.test_user.username
    )

    context.storage_state(path=settings.browser_state_file)
    browser.close()


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=settings.browser_state_file
    )
    page = context.new_page()
    yield page
    browser.close()
