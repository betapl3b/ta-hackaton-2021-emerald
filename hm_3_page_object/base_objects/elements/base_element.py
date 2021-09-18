from hm_3_page_object.helpers.browser import Browser
from selenium.webdriver.remote.webdriver import WebElement
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BaseElement:
    """
    Базовый класс элемента на страницу
    """

    def __init__(self, value, name, by=None, parent=None):
        self._name = name
        self._parent = parent
        self._selector_type = by
        self._selector = value
        self._element_timeout = 5

    @property
    def element_description(self):
        return f"element with {self._selector_type}='{self._selector}'"

    @property
    def _element(self):
        Browser().logger.debug(f"Trying to find element {self.element_description}")
        if isinstance(self._parent, BaseElement):
            element = self._parent._element.find_element(by=self._selector_type, value=self._selector)
        elif isinstance(self._parent, WebElement):
            element = self._parent.find_element(by=self._selector_type, value=self._selector)
        else:
            element = Browser().get_element(selector_type=self._selector_type,
                                            selector=self._selector,
                                            timeout=self._element_timeout)
        Browser().logger.debug(f"Found {self.element_description}")
        Browser().scroll_to(element)
        return element

    def is_present(self):
        try:
            return isinstance(self._element, WebElement)
        except TimeoutException:
            return False

    def not_present(self):
        try:
            Browser().driver.find_element(self._selector_type, self._selector)
            return False
        except NoSuchElementException:
            return True

    def is_displayed(self):
        try:
            return self._element.is_displayed()
        except TimeoutException:
            return False

    def not_displayed(self):
        try:
            return not Browser().driver.find_element(self._selector_type, self._selector)
        except NoSuchElementException:
            return True

    @property
    def text(self):
        return self._element.text

    @property
    def element_timeout(self):
        return self._element_timeout

    @property
    def parent(self):
        return self._parent
