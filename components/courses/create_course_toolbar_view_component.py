from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.courses_title = self.page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_new_course_button = self.page.get_by_test_id('courses-list-toolbar-create-course-button')


    def check_courses_title_is_visible(self):
        expect(self.courses_title).to_be_visible()


    def check_create_new_course_button_is_visible(self, is_create_course_disabled=True):
        expect(self.create_new_course_button).to_be_visible()
        if not is_create_course_disabled:
            expect(self.create_new_course_button).to_be_disabled()
        else:
            expect(self.create_new_course_button).to_be_enabled()


    def click_create_new_course_button(self):
        self.create_new_course_button.click()