from playwright.sync_api import sync_playwright, expect

with sync_playwright() as piaywright:
    browser = piaywright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login', wait_until="networkidle")

    # unknown_locator = page.get_by_test_id('unknown')
    # expect(unknown_locator).to_be_visible()
    #
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('Test')

    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)

    page.wait_for_timeout(3000)
