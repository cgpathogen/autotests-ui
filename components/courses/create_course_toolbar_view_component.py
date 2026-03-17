from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text
import allure

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.courses_title = Text(page, "courses-list-toolbar-title-text", 'courses_title')
        self.create_new_course_button = Button(page, 'courses-list-toolbar-create-course-button', 'course_button')


    # здесь allure шаг уже добавлен в base_element.check_visible()
    def check_courses_title_is_visible(self):
        self.courses_title.check_visible()

    @allure.step('Create new course button is visible')
    def check_create_new_course_button_is_visible(self, is_create_course_disabled=True):
        self.create_new_course_button.check_visible()
        if not is_create_course_disabled:
            self.create_new_course_button.check_disabled()
        else:
            self.create_new_course_button.check_enabled()


    def click_create_new_course_button(self):
        self.create_new_course_button.click()