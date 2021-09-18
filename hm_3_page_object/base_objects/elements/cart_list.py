from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.base_objects.elements.clickable_element import ClickableElement
from selenium.webdriver.common.by import By


class CartList(BaseElement):
    """
    Class for items in Cart
    """

    @property
    def rows(self):
        rows = []
        for i in range(len(self._element.find_elements_by_class_name('item__list--item'))):
            rows.append(
                CartListItem(by=By.XPATH, value=f'(//li[@class=\'item__list--item\'])[{i + 1}]', name='Cart Item'))
        return rows


class CartListItem(BaseElement):
    """
    Class for Item in List Items
    button.btn.btn-default.js-cartItemDetailBtn
    """
    remove_button = ClickableElement(by=By.CSS_SELECTOR, value='button.btn.btn-default.js-cartItemDetailBtn',
                                     name='Remove Button')

    def __init__(self, value, name, by):
        self._attributes = None
        super().__init__(value, name, by)

    @property
    def elements(self):
        if self._attributes is None:
            self._attributes = self.text.split('\n')

        return self._attributes

    @property
    def name(self):
        return self._attributes[0]

    @property
    def code(self):
        return self._attributes[1]

    @property
    def size(self):
        return self._attributes[2]

    @property
    def style(self):
        return self._attributes[3]

    @property
    def stock(self):
        return self._attributes[4]

    @property
    def price(self):
        return self._attributes[5]

    @property
    def delivery(self):
        return self._attributes[6].split(' ')[0]

    @property
    def total_price(self):
        return self._attributes[6].split(' ')[1]
