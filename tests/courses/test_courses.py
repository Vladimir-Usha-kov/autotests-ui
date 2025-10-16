import time
import allure
import pytest
from data.data import CourseCardFormParams, CheckVisibleCourseCardParams
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeatures
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty course list')
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title('Create course')
    def test_create_course(self, create_courses_page: CreateCoursePage, courses_list_page: CoursesListPage):
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
            CourseCardFormParams(title='Playwright', description='Playwright', estimated_time='2 weeks',
                                 max_score='100',
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

    @allure.title('Edit course')
    def test_edit_course(self, create_courses_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_courses_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_courses_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_courses_page.image_upload_widget.check_visible_image_upload_view(is_image_uploaded=True)
        create_courses_page.create_course_form.fill(
            CourseCardFormParams(title='Playwright', description='Playwright', estimated_time='2 weeks',
                                 max_score='100',
                                 min_score='10'))
        create_courses_page.create_course_toolbar.click_button()
        courses_list_page.course_view.check_visible_card(CheckVisibleCourseCardParams(
            index=0,
            title='Playwright',
            estimated_time='2 weeks',
            max_score='100',
            min_score='10'
        ))
        courses_list_page.course_view.menu.click_edit(index=0)
        create_courses_page.create_course_form.fill(CourseCardFormParams(
            title='PlayTest', description='vay', estimated_time='1 weeks',
            max_score='10',
            min_score='1'
        ))
        create_courses_page.create_course_toolbar.click_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible_card(CheckVisibleCourseCardParams(
            index=0,
            title='PlayTest',
            estimated_time='1 weeks',
            max_score='10',
            min_score='1'
        ))