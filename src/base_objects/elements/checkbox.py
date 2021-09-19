from src.base_objects.elements.clickable_element import ClickableElement


class Checkbox(ClickableElement):
    """
    Класс, описывающий чекбокс
    """

    def is_marked(self):
        return self._element.find_element_by_xpath('./input').is_selected()

    def mark(self):
        if not self.is_marked():
            return self._element.click()
