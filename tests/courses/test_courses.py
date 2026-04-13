import pytest
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from playwright.sync_api import Page
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from pages.create_course_page import CreateCoursePage
from pages.courses_page import CoursesPage
from components.courses.create_course_form_component import CreateCourseFormComponent
from tools.routes import AppRoute
from config import settings


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:

    @pytest.mark.courses
    @pytest.mark.regression
    @allure.title("Empty course visibility")
    def test_empty_courses_list(self,
            initialize_browser_state,
            chromium_page: Page,
            courses_page: CoursesPage
    ):
        create_course_form_component = CreateCourseToolbarViewComponent(chromium_page)
        chromium_page.goto(AppRoute.COURSES)
        courses_page.navbar.check_visibility("UI Course", settings.test_user.username)
        courses_page.sidebar.check_visible()
        create_course_form_component.check_courses_title_is_visible()
        create_course_form_component.check_create_new_course_button_is_visible()
        create_course_form_component.click_create_new_course_button()


    @pytest.mark.courses
    @pytest.mark.regression
    @allure.title("Course creation")
    def test_create_course(self, create_course_page: CreateCoursePage, courses_page: CoursesPage, chromium_page: Page):

        create_course_form_component = CreateCourseFormComponent(chromium_page) # компонент
        create_course_exercises_toolbar_view_component = CreateCourseExercisesToolbarViewComponent(chromium_page)

        create_course_page.open(AppRoute.CREATE)
        create_course_page.check_visible_create_course_title("Create course")
        create_course_page.check_disabled_create_course_button()
        create_course_page.check_visible_image_preview_empty_view("No image selected","Preview of selected image will be displayed here")
        create_course_page.check_visible_image_upload_view('Tap on "Upload image" button to select file',"Recommended file size 540X300")
        # компонент добавлены тут
        create_course_exercises_toolbar_view_component.check_visible("Exercises")
        create_course_page.check_visible_exercises_empty_view('There is no exercises','Click on "Create exercise" button to create new exercise')
        create_course_page.upload_image(settings.test_data.image_png_file)
        create_course_page.check_visible_image_remove_view('Tap on "Upload image" button to select file','Recommended file size 540X300')
        # компоненты добавлены тут
        create_course_form_component.check_visible("","","","0","0")
        create_course_form_component.fill("Playwright","2 weeks","Playwright","100","10")

        create_course_page.click_create_course_button()

        courses_page.check_courses_title_is_visible()
        courses_page.check_visible_course_card()


    @pytest.mark.courses
    @pytest.mark.regression
    @allure.title("Edition of course")
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_page: CoursesPage, chromium_page: Page):

        create_course_page.open(AppRoute.CREATE)

        # создаём курс
        create_course_page.upload_image(settings.test_data.image_png_file)
        create_course_page.create_course_form_component.fill("Playwright", "2 weeks", "Playwright", "100", "10")
        create_course_page.click_create_course_button()
        courses_page.check_courses_title_is_visible()
        courses_page.check_visible_course_card()

        # редактируем курс
        create_course_page.click_edit_course_button()
        create_course_page.fill_form(
            "Playwright_edited",
            "3 weeks",
            "Playwright_edited",
            "150",
            "100"
        )
        create_course_page.click_create_course_button()
        courses_page.check_courses_title_is_visible()
        courses_page.check_visible_course_card()
        create_course_page.check_visible_after_fix(
            0,
            "Playwright_edited",
            "150",
            "100",
            "3 weeks")
