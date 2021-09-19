from src.base_objects.base_page import BasePage
from src.base_objects.elements.clickable_element import ClickableElement
from src.base_objects.elements.base_element import BaseElement
from src.base_objects.elements.cart_list import CartList
from src.base_objects.elements.checkbox import Checkbox
from src.base_objects.elements.dropdown import Dropdown
from src.base_objects.elements.input import Input

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
    first_checkout_button = ClickableElement(
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
    second_checkout_button = ClickableElement(
        by=By.XPATH,
        value='(//button[contains(text(), "Check Out")])[2]',
        name='second checkout button')
    choose_country = Dropdown(by=By.ID, value='address.country', name='Country/region dropdown')
    name_input = Input(by=By.ID, value='address.firstName', name='First name')
    surname_input = Input(by=By.ID, value='address.surname', name='Surname')
    address_input = Input(by=By.ID, value='address.line1', name='address')
    city_input = Input(by=By.ID, value='address.townCity', name='city address')
    postcode_input = Input(by=By.ID, value='address.postcode', name='postcode')
    next_button = ClickableElement(by=By.ID, value='addressSubmit', name='next button')
    submit_button = ClickableElement(by=By.ID, value='deliveryMethodSubmit', name='submit button')
    choose_card_type = Dropdown(by=By.ID, value='card_cardType', name='Card type dropdown')
    account_number_input = Input(by=By.ID, value='card_accountNumber', name='account number')
    choose_exp_month = Dropdown(by=By.ID, value='ExpiryMonth', name='Card exp month')
    choose_exp_year = Dropdown(by=By.ID, value='ExpiryYear', name='Card exp year')
    account_cvc = Input(by=By.ID, value='card_cvNumber', name='card cvc')
    next_payment_button = ClickableElement(
        by=By.XPATH, value='//button[@class="btn btn-primary btn-block submit_silentOrderPostForm checkout-next"]',
        name='next payment button')
    terms_checkbox = Checkbox(by=By.ID, value='Terms1', name='terms')
    place_order_button = ClickableElement(by=By.ID, value='placeOrder', name='place order button')
    thanks_notification = BaseElement(by=By.XPATH, value='//div[@class="checkout-success__body__headline"]',
                                      name='Order placed notification')


