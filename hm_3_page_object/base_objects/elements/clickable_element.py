import allure
from hm_3_page_object.base_objects.elements.base_element import BaseElement


class ClickableElement(BaseElement):
    """
    Класс кликабельных элементов
    """

    def click(self):
        with allure.step(f'Open page {self._name}'):
            self._element.click()
