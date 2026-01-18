from playwright.sync_api import expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    courses_main_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_main_title).to_have_text("Courses")

    empty_folder_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(empty_folder_icon).to_be_visible()

    no_results_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_results_title).to_have_text("There is no results")

    results_info_paragraph = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(results_info_paragraph).to_have_text("Results from the load test pipeline will be displayed here")