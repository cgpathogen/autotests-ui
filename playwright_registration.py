from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

    # user data

    user_email = "user.name@gmail.com"
    user_name = "username"
    user_password = "password"

    # locators

    email_input_locator = ('//input[@id=":r0:"]')
    password_input_locator = ('//input[@id=":r1:"]')
    name_input_locator = ('//input[@id=":r2:"]')
    registration_button_locator = ("button#registration-page-registration-button")
    dashboard_title_locator = ("//h6[@data-testid='dashboard-toolbar-title-text']")

    # actions

    page.goto(url)
    page.fill(email_input_locator, user_email)
    page.fill(name_input_locator, user_name)
    page.fill(password_input_locator, user_password)
    page.click(registration_button_locator)
    expect(page.locator(dashboard_title_locator)).to_be_visible()
    page.wait_for_timeout(2000)