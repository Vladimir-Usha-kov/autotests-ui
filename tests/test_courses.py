import time
from sys import excepthook
import pytest
from playwright.sync_api import sync_playwright, expect, Page

from data.data import CourseCardFormParams, CheckVisibleCourseCardParams
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_courses_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_courses_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_courses_page.create_course_toolbar.check_visible(is_disabled_button=True)
    create_courses_page.image_upload_widget.check_visible_image_upload_view(is_image_uploaded=False)
    create_courses_page.create_course_form.check_visible(
        CourseCardFormParams(title='', description='', estimated_time='', max_score='0', min_score='0'))

    create_courses_page.create_exercises_toolbar.check_visible()
    create_courses_page.check_visible_exercises_empty_view()

    create_courses_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_courses_page.image_upload_widget.check_visible_image_upload_view(is_image_uploaded=True)

    create_courses_page.create_course_form.fill(
        CourseCardFormParams(title='Playwright', description='Playwright', estimated_time='2 weeks', max_score='100',
                             min_score='10'))

    create_courses_page.create_course_toolbar.click_button()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible_card(
        CheckVisibleCourseCardParams(
            index=0,
            title='Playwright',
            estimated_time='2 weeks',
            max_score='100',
            min_score='10')
    )
