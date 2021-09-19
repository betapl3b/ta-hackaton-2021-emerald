from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.base_objects.elements.checkbox import Checkbox
from selenium.webdriver.common.by import By


class CategoriesList(BaseElement):
    """
    Class for items in Cart
    """

    @property
    def list(self):
        res = []
        category_item_list = self._element.find_elements_by_xpath(".//li")
        for i in range(len(category_item_list)):
            res.append(
                CategoryItem(by=By.XPATH,
                             value=f"//input[@type='checkbox']/parent::label//span[contains(text(), '{category_item_list[i].text.split('(')[0][:-2].capitalize()}')]",
                             name='category item')
            )
        return res


class CategoryItem(Checkbox):

    def __init__(self, value, name, by):
        super().__init__(value, name, by)

    def select(self):
        self.click()