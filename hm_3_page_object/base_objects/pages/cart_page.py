from hm_3_page_object.base_objects.base_page import BasePage
from hm_3_page_object.base_objects.elements.clickable_element import ClickableElement
from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.base_objects.elements.cart_list import CartList

from selenium.webdriver.common.by import By


class CartPage(BasePage):
    # cart_id not exist for empty carts
    cart_id = BaseElement(by=By.CLASS_NAME, value='cart__id', name='cart id')
    new_cart = ClickableElement(by=By.XPATH, value='//a[contains(text(), "New Cart")]', name='New cart link')

    cart_elements_count = BaseElement(by=By.CSS_SELECTOR,
                                      value='div.js-cart-top-totals.cart__top--totals',
                                      name='Elements in cart')
    cart_elements_sum = BaseElement(by=By.CLASS_NAME,
                                    value='cart__top--amount',
                                    name='Summ of elements in cart')
    first_export_csv = ClickableElement(by=By.XPATH, value='(//a[@class="export__cart--link"])[1]',
                                        name='First export CSV link')
    first_continue_shop_button = BaseElement(
        by=By.XPATH,
        value='(//button[contains(text(), "Continue Shopping")])[1]',
        name='first continue shopping button')
    first_checkout_button = BaseElement(
        by=By.XPATH,
        value='(//button[contains(text(), "Check Out")])[1]',
        name='first checkout button')

    items = CartList(by=By.CSS_SELECTOR, value='ul.item__list.item__list__cart', name='List with items in cart')

    second_export_csv = ClickableElement(by=By.XPATH, value='(//a[@class="export__cart--link"])[2]',
                                         name='Second export CSV link')
    second_continue_shop_button = BaseElement(
        by=By.XPATH,
        value='(//button[contains(text(), "Continue Shopping")])[2]',
        name='second continue shopping button')
    second_checkout_button = BaseElement(
        by=By.XPATH,
        value='(//button[contains(text(), "Check Out")])[2]',
        name='second checkout button')
