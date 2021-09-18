from hm_3_page_object.base_objects.elements.input import Input


class Dropdown(Input):
    """
    Класс, описывающий объект дропдаун
    """

    @property
    def options(self):
        elements = self._element.find_elements_by_css_selector('select option')
        return elements

    def choose_by_value(self, value):
        element = None
        for option in self.options:
            if option.text == value:
                option.click()
                element = option
                break
        return element
