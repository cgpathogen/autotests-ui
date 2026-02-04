import pytest
from playwright.sync_api import expect, Page
from pages.create_course_page import CreateCoursePage
from pages.courses_page import CoursesPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(
        initialize_browser_state,
        chromium_page: Page,
        courses_page: CoursesPage
):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    # В итоге автотест test_empty_courses_list должен проверять следующие элементы:
    # Отображение компонента Navbar — проверяет, что компонент Navbar корректно отображается на странице.
    courses_page.navbar.check_visibility("UI Course", "username")
    # Отображение компонента Sidebar — проверяет, что компонент Sidebar виден и корректно отрисован.
    courses_page.sidebar.check_visible()

    # Отображение заголовка "Courses" — проверяет наличие и корректное отображение заголовка страницы.
    courses_page.check_courses_title_is_visible()
    # Отображение кнопки создания курса — проверяет, что кнопка для создания нового курса отображается.
    courses_page.check_create_new_course_button_is_visible()
    # Отображение пустого блока с текстом "There is no results" —
    # проверяет, что при отсутствии курсов отображается соответствующий блок с сообщением об отсутствии результатов.
    courses_page.check_no_results_title_is_visible()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage,courses_page: CoursesPage):
    create_course_page.open("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title("Create course")
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view("No image selected","Preview of selected image will be displayed here")
    create_course_page.check_visible_image_upload_view('Tap on "Upload image" button to select file',"Recommended file size 540X300")
    create_course_page.check_visible_create_course_form()
    create_course_page.check_visible_exercises_title("Exercises")
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view('There is no exercises','Click on "Create exercise" button to create new exercise')
    create_course_page.upload_image("/Users/anatoly_bobrov/PycharmProjects/autotests-ui/testdata/files/image.png")
    create_course_page.check_visible_image_remove_view('Tap on "Upload image" button to select file','Recommended file size 540X300')
    create_course_page.fill_create_course_form("Playwright","2 weeks","Playwright","100","10")
    create_course_page.click_create_course_button()

    courses_page.check_courses_title_is_visible()
    courses_page.check_create_new_course_button_is_visible()
    courses_page.check_visible_course_card()