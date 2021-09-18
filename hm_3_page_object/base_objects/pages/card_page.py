from hm_3_page_object.base_objects.elements.clickable_element import ClickableElement
from hm_3_page_object.base_objects.elements.base_element import BaseElement

from selenium.webdriver.common.by import By


class CardPage:
    product_title = BaseElement(by=By.XPATH, value='//div[@class="product-details page-title"]/div',
                                name='Page title')
    page_title = BaseElement(by=By.XPATH, value='//h1', name='Product review summery')
    product_price = BaseElement(by=By.XPATH, value='//div[@class="product-details"]/p[@class="price"]',
                                name='Product price')
    add_to_cart_button = ClickableElement(by=By.ID, value='addToCartButton', name='Add to cart button')
    checkout_button = ClickableElement(by=By.XPATH, value='//a[@class="btn btn-primary btn-block add-to-cart-button"]',
                                       name='Checkout button')