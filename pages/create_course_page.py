from pages.base_page import BasePage
from playwright.sync_api import Page, expect

from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.courses_view_component import CourseViewComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from components.courses.image_upload_widget_component import ImageUploadWidgetComponent

from elements.text import Text
from elements.button import Button
from elements.image import Image
from elements.file_input import FileInput



class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.courses_view_component = CourseViewComponent(page)
        self.course_view_menu_component = CourseViewMenuComponent(page)
        self.create_course_form_component = CreateCourseFormComponent(page)
        self.create_course_exercises_toolbar_view_component = CreateCourseExercisesToolbarViewComponent(page)
        self.image_upload_widget_component = ImageUploadWidgetComponent(page,identifier='create-course-preview')


        self.file_input = FileInput(page,"create-course-preview", 'file_input')

        self.create_course_title = Text(page, "create-course-toolbar-title-text", "course_title")
        self.create_course_button = Button(page, "create-course-toolbar-create-course-button","button")
        self.no_image_selected_icon = Image(page, "create-course-preview-empty-view-icon", "selected_icon")
        self.no_image_selected_title = Text(page,"create-course-preview-empty-view-title-text", "selected_title")
        self.no_image_selected_subtitle = Text(page, "create-course-preview-empty-view-description-text", "selected_subtitle")

        self.upload_image_icon = Image(page, "create-course-preview-image-upload-widget-info-icon", "upload_image_icon")
        self.upload_image_title = Text(page,"create-course-preview-image-upload-widget-info-title-text","image_title")
        self.remove_image_button = Button(page, "create-course-preview-image-upload-widget-remove-button","remove_image_button")
        self.upload_image_subtitle = Text(page, "create-course-preview-image-upload-widget-info-description-text", "upload_image_subtitle")
        self.upload_image_button = Button(page, "create-course-preview-image-upload-widget-input", "upload_image_button")

        self.empty_courses_block_icon = Image(page, "create-course-exercises-empty-view-icon", "block_icon")
        self.empty_courses_block_title = Text(page, "create-course-exercises-empty-view-title-text", "block_title")
        self.empty_courses_block_subtitle = Text(page, 'create-course-exercises-empty-view-description-text', "block_subtitle")


    def check_visible_create_course_title(self, value: str):
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text(value)


    def click_create_course_button(self):
        self.create_course_button.click()


    def check_create_course_button_is_visible(self):
        self.create_course_button.check_visible()


    def check_disabled_create_course_button(self):
        self.create_course_button.check_disabled()


    def check_visible_image_preview_empty_view(self, title: str, subtitle: str):
        self.no_image_selected_icon.check_visible()
        self.no_image_selected_title.check_visible()
        self.no_image_selected_title.check_have_text(title)
        self.no_image_selected_subtitle.check_visible()
        self.no_image_selected_subtitle.check_have_text(subtitle)


    def check_visible_image_upload_view(self, title: str, subtitle: str):
        self.upload_image_icon.check_visible()
        self.upload_image_title.check_visible()
        self.upload_image_title.check_have_text(title)
        self.upload_image_subtitle.check_visible()
        self.upload_image_subtitle.check_have_text(subtitle)


    def upload_image(self, path: str):
        self.image_upload_widget_component.upload_preview_image(path)


    def check_visible_image_remove_view(self, title: str, subtitle: str):
        self.remove_image_button.check_visible()
        self.upload_image_button.check_visible()
        self.upload_image_title.check_have_text(title)
        self.upload_image_subtitle.check_have_text(subtitle)


    def check_visible_create_course_form(
            self,
            title_course:str,
            estimated_time: str,
            course_description:str,
            max_score:str,
            min_score:str
    ):
        self.create_course_form_component.check_visible(
            title_course=title_course,
            estimated_time=estimated_time,
            course_description=course_description,
            max_score=max_score,
            min_score=min_score
        )


    def check_visible_exercises_title(self, title: str):
        self.create_course_exercises_toolbar_view_component.check_visible(title)


    def check_visible_exercises_empty_view(self, title: str, subtitle: str):
        self.empty_courses_block_icon.check_visible()

        self.empty_courses_block_title.check_visible()
        self.empty_courses_block_title.check_have_text(title)
        self.empty_courses_block_subtitle.check_visible()
        self.empty_courses_block_subtitle.check_have_text(subtitle)


    def click_edit_course_button(self):
        self.course_view_menu_component.click_edit()


    def fill_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.create_course_form_component.fill(
            title=title,
            estimated_time=estimated_time,
            description=description,
            max_score=max_score,
            min_score=min_score
        )


    def check_visible_after_fix(self, index: int, title: str, max_score: str, min_score: str, estimated_time: str):
        self.courses_view_component.check_visible(
            index=index,
            title=title,
            max_score=max_score,
            min_score=min_score,
            estimated_time=estimated_time
        )