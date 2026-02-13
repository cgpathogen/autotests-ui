from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.charts.chart_view_component import ChartViewComponent


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('dashboard-toolbar-title-text')
        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")


    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Dashboard')


    def check_charts_view_visibility(self):
        self.scores_chart_view.check_visible()
        self.courses_chart_view.check_visible()
        self.students_chart_view.check_visible()
        self.activities_chart_view.check_visible()
