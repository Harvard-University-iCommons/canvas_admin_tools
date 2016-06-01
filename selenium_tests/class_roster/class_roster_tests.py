
from selenium_tests.class_roster.class_roster_base_test_case \
    import ClassRosterBaseTestCase



class ClassRosterTests(ClassRosterBaseTestCase):

    def test_class_roster_url_link(self):

        """
        TLT-1767:  This test checks to make sure that the class roster URL
        contains values that matches the expected values
        AC #6, Test Case #9
        """
        course_name_display = self.test_settings['roster_text_display']
        url_link_course_number = self.test_settings['url_link_course_number']

        # Get the link URL matching the course name display
        link_url = self.main_page.get_link_url(course_name_display)

        # Verify that the expect course number appears in the link URL
        self.assertTrue(url_link_course_number in link_url,
                        "Expected class number does not appear in the class "
                        "roster's URL")
