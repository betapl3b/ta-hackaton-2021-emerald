from src.base_objects.elements.clickable_element import ClickableElement


class Radio(ClickableElement):
    """
    Класс, описывающий радиобаттон
    """

    def is_selected(self):
        return self._element.find_element_by_xpath('./input[@type=\'radio\']').is_selected()

    def select(self):
        if not self.is_selected():
            return self._element.click()
