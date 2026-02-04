import pytest
from playwright.sync_api import expect, Page
from pages.create_course_page import CreateCoursePage
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
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_page.navbar.check_visibility("UI Course", "username")
    courses_page.sidebar.check_visible()

    courses_page.check_create_new_course_button_is_visible()
    courses_page.check_no_results_title_is_visible()