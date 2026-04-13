import pytest
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from playwright.sync_api import Page
from pages.dashboard_page import DashboardPage
from pages.courses_page import CoursesPage
from tools.routes import AppRoute


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:

    @pytest.mark.courses
    @pytest.mark.regression
    @allure.title("Dashboard visibility checking")
    def test_dashboard_displaying(self,
            initialize_browser_state,
            chromium_page: Page,
            courses_page: CoursesPage,
            dashboard_page: DashboardPage
    ):
        chromium_page.goto(AppRoute.DASHBOARD)

        courses_page.navbar.check_visibility("UI Course", "username")
        courses_page.sidebar.check_visible()
        dashboard_page.dashboard_toolbar_view_component.check_visible() # добавил компонент тут
        dashboard_page.dashboard_toolbar_view_component.check_charts_view_visibility() # добавил компонент тут