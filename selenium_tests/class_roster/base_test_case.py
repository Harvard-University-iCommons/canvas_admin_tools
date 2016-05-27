from django.conf import settings
from os.path import abspath, dirname, join


from selenium_tests.course_admin.course_admin_base_test_case \
    import CourseAdminBaseTestCase
from selenium_tests.course_admin.page_objects\
    .course_admin_dashboard_page_object import CourseAdminDashboardPage
from selenium_tests.class_roster.page_objects.class_roster_main_page import \
    MainPageObject


class ClassRosterBaseTestCase(CourseAdminBaseTestCase):

    def setUp(self):
        """
        Redirects browser to test course URL and login to PIN using
        specified credentials.
        """
        super(CourseAdminBaseTestCase, self).setUp()

        # instantiate
        self.dashboard_page = CourseAdminDashboardPage(self.driver)
        self.class_roster_page = MainPageObject(self.driver)
        #TODO: Need to non changing test URL to point tests to
        self.test_settings = settings.SELENIUM_CONFIG['class_roster']

        # initialize
        if not self.dashboard_page.is_loaded():
            self.dashboard_page.get(self.TOOL_URL)

        # navigate to cross-list tool
        self.dashboard_page.select_class_roster_link()

        # check if page is loaded (which will also set the focus on the tool)
        self.assertTrue(self.class_roster_page.is_loaded())
