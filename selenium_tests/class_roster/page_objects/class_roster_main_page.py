"""
This file models the Class Roster Main (Landing) Page
"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium_tests.class_roster.page_objects.class_roster_base_page_object \
    import ClassRosterBasePageObject


class Locators(object):
    CLASS_ROSTER_BREADCRUMB = (By.XPATH, './/h1[contains(., "Class Roster")]')

    @classmethod
    def FIND_LINK_TEXT(cls, text_value):
        """
        Locates the link based on partial link text, given the text value
        """
        return By.PARTIAL_LINK_TEXT, "{}".format(text_value)


class MainPageObject(ClassRosterBasePageObject):
    page_loaded_locator = Locators.CLASS_ROSTER_BREADCRUMB

    def get_link_url(self, text_value):
        """
        Returns the URL from the partial link text passed in from tests.
        """
        try:
            link = self.find_element(*Locators.FIND_LINK_TEXT(text_value))
            # Get the URL of the link element
            link_url = link.get_attribute('href')
        except NoSuchElementException:
            return False
        return link_url
