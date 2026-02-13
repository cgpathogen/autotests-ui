import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.create_course_page import CreateCoursePage
from pages.courses_page import CoursesPage


@pytest.fixture(scope="function")
def login_page(chromium_page: LoginPage) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture(scope="function")
def registration_page(chromium_page: RegistrationPage) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)


@pytest.fixture(scope="function")
def dashboard_page(chromium_page: DashboardPage) -> DashboardPage:
    return DashboardPage(page=chromium_page)


@pytest.fixture(scope="function")
def create_course_page(chromium_page: CreateCoursePage) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page)


@pytest.fixture(scope="function")
def courses_page(chromium_page: CoursesPage) -> CoursesPage:
    return CoursesPage(page=chromium_page)