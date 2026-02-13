from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_toolbar_view_component = CreateCourseToolbarViewComponent(self.page)
        self.create_course_exercises_toolbar_view_component = CreateCourseExercisesToolbarViewComponent(self.page)

        self.title_course_input = self.page.get_by_test_id("create-course-form-title-input").locator("input")
        self.estimated_time_input = self.page.get_by_test_id("create-course-form-estimated-time-input").locator("input")
        self.course_description_input = self.page.get_by_test_id("create-course-form-description-input").locator(
            "textarea").first
        self.max_score_input = self.page.get_by_test_id("create-course-form-max-score-input").locator("input")
        self.min_score_input = self.page.get_by_test_id("create-course-form-min-score-input").locator("input")


    def check_visible(self):
        expect(self.title_course_input).to_be_visible()
        expect(self.estimated_time_input).to_be_visible()
        expect(self.course_description_input).to_be_visible()
        expect(self.max_score_input).to_be_visible()
        expect(self.min_score_input).to_be_visible()


    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_course_input.fill(title)
        expect(self.title_course_input).to_have_value(title)

        self.estimated_time_input.fill(estimated_time)
        expect(self.estimated_time_input).to_have_value(estimated_time)

        self.course_description_input.fill(description)
        expect(self.course_description_input).to_have_value(description)

        self.max_score_input.fill(max_score)
        expect(self.max_score_input).to_have_value(max_score)

        self.min_score_input.fill(min_score)
        expect(self.min_score_input).to_have_value(min_score)