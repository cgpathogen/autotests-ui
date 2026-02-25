from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_toolbar_view_component = CreateCourseToolbarViewComponent(self.page)
        self.create_course_exercises_toolbar_view_component = CreateCourseExercisesToolbarViewComponent(self.page)

        self.title_course_input = Input(self.page, "create-course-form-title-input", 'title_input')
        self.estimated_time_input = Input(self.page, "create-course-form-estimated-time-input",'estimated_time_input')
        self.course_description_input = Textarea(self.page, "create-course-form-description-input", "textarea")
        self.max_score_input = Input(self.page, "create-course-form-max-score-input", 'max_score_input')
        self.min_score_input = Input(self.page, "create-course-form-min-score-input", 'min_score_input')


    def check_visible(self):
        self.title_course_input.check_visible()
        self.estimated_time_input.check_visible()
        self.course_description_input.check_visible()
        self.max_score_input.check_visible()
        self.min_score_input.check_visible()


    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_course_input.fill(title)
        self.title_course_input.check_have_value(title)

        self.estimated_time_input.fill(estimated_time)
        self.estimated_time_input.check_have_value(estimated_time)

        self.course_description_input.fill(description)
        self.course_description_input.check_have_value(description)

        self.max_score_input.fill(max_score)
        self.max_score_input.check_have_value(max_score)

        self.min_score_input.fill(min_score)
        self.min_score_input.check_have_value(min_score)