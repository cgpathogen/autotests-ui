from pages.base_page import BasePage
from playwright.sync_api import expect
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_components import SidebarComponent


class CoursesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.courses_title = self.page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_new_course_button = self.page.get_by_test_id('courses-list-toolbar-create-course-button')
        self.no_results_title = self.page.get_by_test_id("courses-list-empty-view-title-text")

        self.created_course_title = self.page.get_by_test_id("course-widget-title-text")
        self.created_course_max_score = self.page.get_by_test_id("course-max-score-info-row-view-text")
        self.created_course_min_score = self.page.get_by_test_id("course-min-score-info-row-view-text")
        self.created_course_estimated_time = self.page.get_by_test_id("course-estimated-time-info-row-view-text")


    def check_courses_title_is_visible(self):
        expect(self.courses_title).to_be_visible()


    def check_no_results_title_is_visible(self):
        expect(self.no_results_title).to_be_visible()
        expect(self.no_results_title).to_have_text("There is no results")


    def check_visible_course_card(self, index=0):
        expect(self.created_course_title.nth(index)).to_be_visible()
        expect(self.created_course_max_score.nth(index)).to_be_visible()
        expect(self.created_course_min_score.nth(index)).to_be_visible()
        expect(self.created_course_estimated_time.nth(index)).to_be_visible()