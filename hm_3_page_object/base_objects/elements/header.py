from selenium.webdriver.common.by import By

from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.base_objects.elements.navigation_bar import NavigationBar


class Header(BaseElement):
    """
    Header class
    """
    EXPAND_SIDEBAR_BUTTON = "//button[@class='btn js-toggle-sm-navigation']"
    LOGIN_SIGN_IN_BUTTON = "//li[@class='liOffcanvas']/a"
    B2C_ACCELERATOR_LOGO = "//main//a/img[@title='hybris Accelerator']"
    SEARCH_FIELD = "//input[@id='js-site-search-input']"
    SEARCH_BUTTON = "//button[@class='js_search_button']"
    FIND_A_STORE_BUTTON = "div.nav-location > a"
    ORDER_TOOL_MENU = "//div[@class='yCmsComponent']//div[contains(@class, 'nav-order-tools js-nav-order-tools')]"
    QUICK_ORDER_BUTTON = "//a[@title='Quick Order']"
    CART_IMPORT_ORDER_BUTTON = "//a[@title='Import Saved Cart']"

    navigation_bar = NavigationBar("//ul[contains(@class, 'nav__links--products js-offcanvas-links')]",
                                   name='navigation_bar', by=By.XPATH)

    def expand_sidebar(self):
        self._element.find_element_by_xpath(self.EXPAND_SIDEBAR_BUTTON).click()

    def click_login_button(self):
        self._element.find_element_by_xpath(self.LOGIN_SIGN_IN_BUTTON)

    def click_b2c_accelerator_logo(self):
        self._element.find_element_by_xpath(self.B2C_ACCELERATOR_LOGO).click()

    def click_search_button(self):
        self._element.find_element_by_xpath(self.SEARCH_BUTTON).click()

    def fill_search_field(self, text):
        self._element.find_element_element_by_xpath(self.SEARCH_FIELD).send_keys(text)

    def click_find_a_store_button(self):
        self._element.find_element_by_css_selector(self.FIND_A_STORE_BUTTON).click()

    def expand_order_tools_menu(self):
        self._element.find_element_by_xpath(self.ORDER_TOOL_MENU).click()

    def click_quick_order(self):
        self._element.find_element_by_xpath(self.QUICK_ORDER_BUTTON).click()

    def click_import_saved_cart(self):
        self._element.find_element_by_xpath(self.CART_IMPORT_ORDER_BUTTON).click()
