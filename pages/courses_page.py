from pages.base_page import BasePage
from playwright.sync_api import expect
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_components import SidebarComponent
from elements.text import Text
from elements.button import Button


class CoursesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.courses_title = Text(page,"courses-list-toolbar-title-text", 'courses_title')
        self.create_new_course_button = Button(page,'courses-list-toolbar-create-course-button','new-course-button')
        self.no_results_title = Text(page,"courses-list-empty-view-title-text",'no_results_title')

        self.created_course_title = Text(page,"course-widget-title-text", 'created_course_title')
        self.created_course_max_score = Text(page,"course-max-score-info-row-view-text", 'created_course_max_score')
        self.created_course_min_score = Text(page, "course-max-score-info-row-view-text", 'created_course_min_score')
        self.created_course_estimated_time = Text(page,"course-estimated-time-info-row-view-text", 'estimated-time')


    def check_courses_title_is_visible(self):
        self.courses_title.check_visible()


    def check_no_results_title_is_visible(self):
        self.no_results_title.check_visible()
        self.no_results_title.check_have_text("There is no results")


    def check_visible_course_card(self, index=0):
        self.created_course_title.check_visible(index)
        self.created_course_max_score.check_visible(index)
        self.created_course_min_score.check_visible(index)
        self.created_course_estimated_time.check_visible(index)