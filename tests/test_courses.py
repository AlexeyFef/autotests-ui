from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
# используем фикстуру chromium_page_with_state для передачи состояние браузера в тест
def test_empty_courses_list(chromium_page_with_state: Page):
        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        title_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(title_courses).to_be_visible()
        expect(title_courses).to_have_text('Courses')

        icon_folder = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_folder).to_be_visible()

        title_there_is_no_results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(title_there_is_no_results).to_be_visible()
        expect(title_there_is_no_results).to_have_text('There is no results')

        courses_empty_view_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_empty_view_description).to_be_visible()
        expect(courses_empty_view_description).to_have_text(
            'Results from the load test pipeline will be displayed here')