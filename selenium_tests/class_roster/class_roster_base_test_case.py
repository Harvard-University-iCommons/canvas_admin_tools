from os.path import abspath, dirname, join
from django.conf import settings
from urlparse import urljoin

from selenium_tests.course_admin.course_admin_base_test_case \
    import CourseAdminBaseTestCase
from selenium_tests.course_admin.page_objects\
    .course_admin_dashboard_page_object import CourseAdminDashboardPage
from selenium_tests.class_roster.page_objects.class_roster_main_page import \
    MainPageObject

# Common files used for all Class Roster test cases
CLASS_ROSTER_PERMISSION_ROLES = join(dirname(abspath(__file__)), 'test_data',
                                     'class_roster_roles_access.xlsx')


class ClassRosterBaseTestCase(CourseAdminBaseTestCase):

    def setUp(self):
        """
        Redirects browser to test course URL and login to PIN using
        specified credentials.
        """
        super(CourseAdminBaseTestCase, self).setUp()

        # instantiate
        dashboard_page = CourseAdminDashboardPage(self.driver)
        main_page = MainPageObject(self.driver)
        test_settings = settings.SELENIUM_CONFIG['class_roster']

        canvas_base_url = test_settings.SELENIUM_CONFIG['canvas_base_url']
        tool_relative_url = test_settings.SELENIUM_CONFIG['course_link']
        tool_url = urljoin(canvas_base_url, tool_relative_url)

        # After setup, override the default automated test URL, which
        # does not have a working class roster, with this course site.
        main_page.get(tool_url)
        main_page.focus_on_tool_frame()

        # Click on the class roster button from the dashboard
        dashboard_page.select_class_roster_link()
        self.assertTrue(self.class_roster_page.is_loaded())
