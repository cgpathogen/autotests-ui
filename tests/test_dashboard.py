import pytest
from playwright.sync_api import Page
from pages.dashboard_page import DashboardPage
from pages.courses_page import CoursesPage


@pytest.mark.courses
@pytest.mark.regression
def test_dashboard_displaying(
        initialize_browser_state,
        chromium_page: Page,
        courses_page: CoursesPage,
        dashboard_page: DashboardPage
):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    courses_page.navbar.check_visibility("UI Course", "username")
    courses_page.sidebar.check_visible()
    dashboard_page.dashboard_toolbar_view_component.check_visible() # добавил компонент тут
    dashboard_page.dashboard_toolbar_view_component.check_charts_view_visibility() # добавил компонент тут