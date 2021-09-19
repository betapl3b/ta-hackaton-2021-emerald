from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.base_objects.elements.clickable_element import ClickableElement
from selenium.webdriver.common.by import By


class ProductGrid(BaseElement):
    """
    Class for items in Cart
    """

    @property
    def list(self):
        res = []
        for i in range(len(self._element.find_elements_by_class_name('product-item'))):
            res.append(
                ProductGridItem(by=By.XPATH, value=f"(//ul[@class='product__listing product__grid']"
                                                   f"//div[@class='product-item'])[{i + 1}]", name='Cart Item'))
        return res


class ProductGridItem(ClickableElement):

    def __init__(self, value, name, by):
        self._attributes = None
        super().__init__(value, name, by)
