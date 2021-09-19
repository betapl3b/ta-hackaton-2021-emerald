from src.base_objects.elements.base_element import BaseElement
from src.helpers.logger import Logger


class ClickableElement(BaseElement):
    """
    Класс кликабельных элементов
    """

    def click(self):
        Logger().debug(f'Clicking {self.element_description}')
        self._element.click()

    def is_enabled(self):
        return self._element.is_enabled()
