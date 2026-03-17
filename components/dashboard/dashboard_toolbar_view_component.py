from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.charts.chart_view_component import ChartViewComponent
from elements.text import Text
import allure

class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(self.page, 'dashboard-toolbar-title-text',"dashboard_title")
        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")

    @allure.step("check title is visible and has text 'Dashboard'")
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Dashboard')


    @allure.step("check chart view is visible")
    def check_charts_view_visibility(self):
        self.scores_chart_view.check_visible()
        self.courses_chart_view.check_visible()
        self.students_chart_view.check_visible()
        self.activities_chart_view.check_visible()
