from playwright.sync_api import sync_playwright, expect

def keyboard(param): # метод для ввода данных с клавиатуры
    for i in param:
        page.keyboard.type(i)

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()

    # проверяем дизэйбл
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    expect(page.locator("//button[@data-testid='registration-page-registration-button']")).to_be_disabled()

    # вводим эмейл
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.focus()
    keyboard("user@gmail.com")

    # вводим юзернейм
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.focus()
    keyboard("username")

    # вводим пароль
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.focus()
    keyboard("password")

    # проверяем энэйбл
    expect(page.locator("//button[@data-testid='registration-page-registration-button']")).to_be_enabled()