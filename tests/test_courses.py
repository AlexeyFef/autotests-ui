from playwright.sync_api import sync_playwright, expect, Page
import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_courses_page import CreateCoursePage


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


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.vizit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0"
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercise_empty_view()
    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_courses_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )

