from src.helpers.browser import Browser
from src.base_objects.elements.clickable_element import ClickableElement
from selenium.webdriver.remote.webdriver import WebElement

from src.helpers.logger import Logger


class Input(ClickableElement):
    """
    Класс для работы с элементами, в которые можно что-нибудь ввести
    """

    def send_keys(self, text):
        self._element.click()
        Logger().debug(f"Sending '{text}' to input {self.element_description}")
        self._element.send_keys(text)
        return self._element

    def __set__(self, instance, value):
        element: WebElement = Browser().get_element(selector_type=self._selector_type,
                                                    selector=self._selector,
                                                    timeout=self.element_timeout)
        Browser().scroll_to(element)
        Browser().driver.execute_script('arguments[0].click()', element)
        element.send_keys(value)

    def clear(self):
        self._element.clear()
        return self._element

    @property
    def value(self):
        return self._element.get_attribute('value')

    @property
    def is_enabled(self):
        return self._element.is_enabled()

    @property
    def is_disabled(self):
        return not self._element.is_enabled()
