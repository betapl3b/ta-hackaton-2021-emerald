from src.base_objects.elements.base_element import BaseElement


class List(BaseElement):
    """
    Класс по работе со списками
    """

    @property
    def rows(self):
        return [row.text for row in
                self._element.find_elements_by_xpath(f'//ul[@class=\'{self._selector.replace(".", " ")}\']/li')]
