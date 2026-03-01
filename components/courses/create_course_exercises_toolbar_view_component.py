from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_title = Text(
            page, "create-course-exercises-box-toolbar-title-text", "exercises_title"
        )
        self.create_course_button = Button(
            page, "create-course-exercises-box-toolbar-create-exercise-button", 'add_course_button'
        )


    def check_visible(self, title_name: str):
        self.exercises_title.check_visible()
        self.exercises_title.check_have_text(title_name)

        self.create_course_button.check_visible()
        self.create_course_button.check_enabled()


    def click_create_exercise_button(self):
        self.create_course_button.click()