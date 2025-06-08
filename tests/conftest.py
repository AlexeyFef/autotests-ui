import pytest
from playwright.sync_api import sync_playwright, Playwright, Page

@pytest.fixture   # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright: Playwright) -> Page: # Аннотируем возвращаемое фикстурой значение
    browser = playwright.chromium.launch(headless=False)    # Запускаем браузер
    yield browser.new_page()                     # Передаем страницу для использования в тесте
    browser.close()                               # Закрываем браузер после выполнения тестов