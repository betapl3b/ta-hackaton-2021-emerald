from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.base_objects.elements.radio import Radio
from hm_3_page_object.base_objects.elements.checkbox import Checkbox
from selenium.webdriver.common.by import By


class Row(BaseElement):
    """
    Класс, описывающий объект div, содержащий несколько одинаковых элементов
    """

    @property
    def radios(self):
        elements = []
        for i in range(len(self._element.find_elements_by_class_name('label-radio'))):
            elements.append(
                Radio(by=By.XPATH, value=f'//label[@class=\'label-radio\'][{i + 1}]', name='radio button'))
        return elements

    @property
    def checkboxes(self):
        elements = []
        for i in range(len(self._element.find_elements_by_class_name('label-checkbox'))):
            elements.append(
                Checkbox(by=By.XPATH, value=f'//label[@class=\'label-checkbox\'][{i + 1}]', name='checkbox'))
        return elements
