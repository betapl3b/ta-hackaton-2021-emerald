from src.base_objects.elements.base_element import BaseElement
from src.base_objects.elements.checkbox import Checkbox
from selenium.webdriver.common.by import By


class ShopCategoriesList(BaseElement):
    """
    Class for items in Cart
    """

    @property
    def list(self):
        res = []
        for i in range(len(self._element.find_elements_by_class_name('facet__results js-facet-container '))):
            res.append(
                ShopCategoryItem(by=By.XPATH, value=f'(//div[@class="facet__results js-facet-container"]//li)[{i + 1}]'
                                                    f'//input[@type=\'checkbox\']',
                                 name='Shop'))
        return res


class ShopCategoryItem(Checkbox):

    def __init__(self, value, name, by):
        super().__init__(value, name, by)

    def select(self):
        self.mark()