
from selenium_tests.class_roster.base_test_case import ClassRosterBaseTestCase
from selenium_tests.class_roster.page_objects.class_roster_main_page \
    import MainPageObject
from selenium_tests.course_admin.page_objects\
    .course_admin_dashboard_page_object import CourseAdminDashboardPage


class ClassRosterTests(ClassRosterBaseTestCase):

    def test_class_roster_url_link(self):

        """
        TLT-1767:  This test checks to make sure that the class roster URL
        contains values that matches the expected values
        AC #6, Test Case #9
        """

        # TODO: Move this into base test case?
        main_page = MainPageObject(self.driver)
        dashboard = CourseAdminDashboardPage(self.driver)

        # Overriding the default automated test URL (which does not have a
        # working class roster list, with this test site)
        # TODO: make URL default link for Course Roster in base test case?
        main_page.get(self.test_settings['course_link'])
        main_page.focus_on_tool_frame()

        # Select the class roster button from the dashboard page
        dashboard.select_class_roster_link()

        # Get the URL containing the link text
        link_url = main_page.get_link_url("JAPAN BA 001")
        print link_url

        # TODO: store values in local.py
        url_link_text = "CLASS_ROSTER"
        url_link_course_number = "14754"

        pusedocode: 
        if link url contains url_link_text:
            return True
        else:
            return "The URL format did not display the expected course number"

