from selenium.webdriver.common.by import By

from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.base_objects.elements.navigation_bar import NavigationBar


class Header(BaseElement):
    """
    Header class
    """
    EXPAND_SIDEBAR_BUTTON = "//button[@class='btn js-toggle-sm-navigation']"

    navigation_bar = NavigationBar("//ul[contains(@class, 'nav__links--products js-offcanvas-links')]",
                                   name='navigation_bar', by=By.XPATH)

    def expand_sidebar(self):
        self._element.find_elements_by_xpath(self.EXPAND_SIDEBAR_BUTTON).click()
