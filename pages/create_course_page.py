from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = self.page.get_by_test_id("create-course-toolbar-title-text")
        self.create_course_button = self.page.get_by_test_id("create-course-toolbar-create-course-button")
        self.no_image_selected_icon = self.page.get_by_test_id("create-course-preview-empty-view-icon")
        self.no_image_selected_title = self.page.get_by_test_id("create-course-preview-empty-view-title-text")
        self.no_image_selected_subtitle = self.page.get_by_test_id("create-course-preview-empty-view-description-text")

        self.upload_image_icon = self.page.get_by_test_id("create-course-preview-image-upload-widget-info-icon")
        self.upload_image_title = self.page.get_by_test_id("create-course-preview-image-upload-widget-info-title-text")
        self.remove_image_button = self.page.get_by_test_id("create-course-preview-image-upload-widget-remove-button")
        self.upload_image_subtitle = self.page.get_by_test_id("create-course-preview-image-upload-widget-info-description-text")
        self.upload_image_button = self.page.get_by_test_id("create-course-preview-image-upload-widget-input")

        self.title_course_input = self.page.get_by_test_id("create-course-form-title-input").locator("input")
        self.estimated_time_input = self.page.get_by_test_id("create-course-form-estimated-time-input").locator("input")
        self.course_description_input = self.page.get_by_test_id("create-course-form-description-input").locator("textarea").first
        self.max_score_input = self.page.get_by_test_id("create-course-form-max-score-input").locator("input")
        self.min_score_input = self.page.get_by_test_id("create-course-form-min-score-input").locator("input")

        self.exercises_title = self.page.get_by_test_id("create-course-exercises-box-toolbar-title-text")
        self.add_course_button = self.page.get_by_test_id("create-course-exercises-box-toolbar-create-exercise-button")

        self.empty_courses_block_icon = self.page.get_by_test_id("create-course-exercises-empty-view-icon")
        self.empty_courses_block_title = self.page.get_by_test_id("create-course-exercises-empty-view-title-text")
        self.empty_courses_block_subtitle = self.page.get_by_test_id('create-course-exercises-empty-view-description-text')


    def check_visible_create_course_title(self, value: str):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text(value)


    def click_create_course_button(self):
        self.create_course_button.click()


    def check_create_course_button_is_visible(self):
        expect(self.create_course_button).to_be_visible()


    def check_disabled_create_course_button(self):
        expect(self.create_course_button).to_be_disabled()


    def check_visible_image_preview_empty_view(self, title: str, subtitle: str):
        expect(self.no_image_selected_icon).to_be_visible()
        expect(self.no_image_selected_title).to_be_visible()
        expect(self.no_image_selected_title).to_have_text(title)
        expect(self.no_image_selected_subtitle).to_be_visible()
        expect(self.no_image_selected_subtitle).to_have_text(subtitle)


    def check_visible_image_upload_view(self, title: str, subtitle: str):
        expect(self.upload_image_icon).to_be_visible()
        expect(self.upload_image_title).to_be_visible()
        expect(self.upload_image_title).to_have_text(title)
        expect(self.upload_image_subtitle).to_be_visible()
        expect(self.upload_image_subtitle).to_have_text(subtitle)


    def upload_image(self, path: str):
        self.upload_image_button.set_input_files(path)


    def check_visible_image_remove_view(self, title: str, subtitle: str):
        expect(self.remove_image_button).to_be_visible()
        expect(self.upload_image_button).to_be_visible()
        expect(self.upload_image_title).to_have_text(title)
        expect(self.upload_image_subtitle).to_have_text(subtitle)


    def check_visible_create_course_form(self):
        expect(self.title_course_input).to_be_visible()
        expect(self.title_course_input).to_have_value("")

        expect(self.estimated_time_input).to_be_visible()
        expect(self.estimated_time_input).to_have_value("")

        expect(self.course_description_input).to_be_visible()
        expect(self.course_description_input).to_have_value("")

        expect(self.max_score_input).to_be_visible()
        expect(self.max_score_input).to_have_value("0")

        expect(self.min_score_input).to_be_visible()
        expect(self.min_score_input).to_have_value("0")


    def check_visible_exercises_title(self, title: str):
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text(title)


    def check_visible_create_exercise_button(self):
       expect(self.add_course_button).to_be_visible()


    def check_visible_exercises_empty_view(self, title: str, subtitle: str):
        expect(self.empty_courses_block_icon).to_be_visible()
        expect(self.empty_courses_block_title).to_be_visible()
        expect(self.empty_courses_block_title).to_have_text(title)
        expect(self.empty_courses_block_subtitle).to_be_visible()
        expect(self.empty_courses_block_subtitle).to_have_text(subtitle)


    def fill_create_course_form(self, title=None, estimated_time=None,description=None, max_score=None, min_score=None):
        self.title_course_input.fill(title)
        self.estimated_time_input.fill(estimated_time)
        self.course_description_input.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)
