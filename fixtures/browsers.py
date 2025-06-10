import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture   # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright: Playwright) -> Page: # Аннотируем возвращаемое фикстурой значение
    browser = playwright.chromium.launch(headless=False)    # Запускаем браузер
    yield browser.new_page()                     # Передаем страницу для использования в тесте
    browser.close()                               # Закрываем браузер после выполнения тестов



@pytest.fixture(scope="session")
# Фикстура регистрирует нового пользователя и сохранять состояние браузера для последующего использования
def initialize_browser_state(playwright: Playwright):
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
    browser.close()



@pytest.fixture()
# Фикстура открывает новую страницу браузера, используя сохраненное состояние из файла browser-state.json
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()
    browser.close()