from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    page.get_by_test_id('login-form-email-input').locator('input').fill("user.name@gmail.com")
    page.get_by_test_id('login-form-password-input').locator('input').fill("password")
    page.get_by_test_id('login-page-login-button').click()

    wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
    page.wait_for_timeout(5000)