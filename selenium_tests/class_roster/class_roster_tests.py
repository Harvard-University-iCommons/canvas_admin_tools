
from selenium_tests.class_roster.class_roster_base_test_case \
    import ClassRosterBaseTestCase



class ClassRosterTests(ClassRosterBaseTestCase):

    def test_class_roster_url_link(self):

        """
        TLT-1767:  This test checks to make sure that the class roster URL
        contains values that matches the expected values
        AC #6, Test Case #9
        """
        roster_text_display = self.test_settings['roster_text_display']
        url_link_course_number = self.test_settings['url_link_course_number']

        # Get the URL containing the link text
        link_url = self.main_page.get_link_url(roster_text_display)
