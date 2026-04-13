from playwright.sync_api import sync_playwright, expect
from tools.routes import AppRoute
from config import settings


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)

    user_email = page.get_by_test_id("registration-form-email-input").locator("input")
    user_email.fill(settings.test_user.email)

    user_name = page.get_by_test_id("registration-form-username-input").locator("input")
    user_name.fill(settings.test_user.username)

    user_password = page.get_by_test_id("registration-form-password-input").locator("input")
    user_password.fill(settings.test_user.password)

    reg_btn = page.get_by_test_id("registration-page-registration-button")
    reg_btn.click()

    context.storage_state(path="data.json")


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(storage_state="data.json")
    page = context.new_page()

    page.goto(AppRoute.COURSES)

    main_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(main_title).to_have_text("Courses")

    folder_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(folder_icon).to_be_visible()

    results_title = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(results_title).to_have_text("There is no results")

    description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(description).to_have_text("Results from the load test pipeline will be displayed here")