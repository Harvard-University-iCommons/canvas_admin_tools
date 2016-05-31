"""
This file models the Class Roster Main (Landing) Page
"""

from selenium.webdriver.common.by import By
from selenium_tests.class_roster.page_objects.class_roster_base_page_object \
    import ClassRosterBasePageObject


class Locators(object):
    CLASS_ROSTER_BREADCRUMB = (By.XPATH, './/h1[contains(., "Class Roster")]')


class MainPageObject(ClassRosterBasePageObject):
        page_loaded_locator = Locators.CLASS_ROSTER_BREADCRUMB
