from src.base_objects.elements.base_element import BaseElement
from src.base_objects.elements.clickable_element import ClickableElement

from selenium.webdriver.common.by import By


class SelectedCategoriesList(BaseElement):
    """
    Class for items in Cart
    """

    @property
    def list(self):
        res = []
        selected_category_item_list = self._element.find_elements_by_xpath(".//li")
        for i in range(len(selected_category_item_list)):
            res.append(
                SelectedCategoryItem(by=By.XPATH,
                                     value=f"//li[contains(text(), '{selected_category_item_list[i].text.split('(')[0][:-1].capitalize()}')]",
                                     name='category item')
            )
        return res


class SelectedCategoryItem(BaseElement):

    def __init__(self, value, name, by):
        super().__init__(value, name, by)

    remove_button = ClickableElement(by=By.XPATH, value="//span[@class='glyphicon glyphicon-remove']",
                                     name='Remove Button')

    def select(self):
        self.click()