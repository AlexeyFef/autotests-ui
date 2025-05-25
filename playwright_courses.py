from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('fafafa@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('fafafa')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')

    page.wait_for_timeout(3000)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    title_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_courses).to_be_visible()
    expect(title_courses).to_have_text('Courses')

    icon_folder = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_folder).to_be_visible()

    title_there_is_no_results = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(title_there_is_no_results).to_be_visible()
    expect(title_there_is_no_results).to_have_text('There is no results')

    title_results_from_the_load_test_pipeline_will_be_displayed_here = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(title_results_from_the_load_test_pipeline_will_be_displayed_here).to_be_visible()
    expect(title_results_from_the_load_test_pipeline_will_be_displayed_here).to_have_text('Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(5000)