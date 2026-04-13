import pytest
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from playwright.sync_api import Page
from components.authentication.registration_form_component import RegistrationFormComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage
from tools.routes import AppRoute
from config import settings


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTIFICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTIFICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:

    @pytest.mark.registration
    @pytest.mark.regression
    @allure.title("Successful user registration")
    def test_successful_registration(
            self,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage,
            chromium_page: Page
    ):
        registration_form_component = RegistrationFormComponent(chromium_page)
        dashboard_toolbar_view_component = DashboardToolbarViewComponent(chromium_page)

        registration_page.open(AppRoute.REGISTRATION)

        registration_form_component.check_visible(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()
        dashboard_toolbar_view_component.check_visible() # добавил компонент тут
