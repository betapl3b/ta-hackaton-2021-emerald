from pytest_bdd import given, when, then

from time import sleep

from src.base_objects.pages.login_page import LoginPage

from src.base_objects.pages.card_page import CardPage
from src.base_objects.pages.cart_page import CartPage
from src.base_objects.base_page import BasePage


@when("Choose product", target_fixture="product_name")
def choose_product():
    product_name = BasePage().product_card_elem_name.text
    BasePage().product_card_elem.click()
    return product_name


@then("Product card is opened")
def product_card_opened(product_name):
    assert product_name in CardPage().product_title.text.upper()
    assert CardPage().page_title.is_displayed()
    assert CardPage().product_price.is_displayed()
    assert CardPage().add_to_cart_button.is_displayed()


@when("Click add product to cart")
def click_add_product(product_name):
    CardPage().add_to_cart_button.click()


@when("Click checkout")
def click_checkout():
    sleep(1)
    CardPage().checkout_button.click()


@when("Click cart checkout")
def click_cart_checkout():
    sleep(1)
    CartPage().second_checkout_button.click()


@when("Fill form")
def fill_form(firstname, lastname):
    CartPage().choose_country = 'Jersey'
    sleep(1)
    CartPage().name_input = firstname
    CartPage().surname_input = lastname
    CartPage().address_input = 'Address'
    CartPage().city_input = 'City'
    CartPage().postcode_input = '123456'
    CartPage().next_button.click()


@when("Submit form")
def submit_form():
    CartPage().submit_button.click()


@when("Fill payment")
def submit_form():
    CartPage().choose_card_type = 'VISA'
    CartPage().account_number_input = '1234123412341234'
    CartPage().choose_exp_month = '01'
    CartPage().choose_exp_year = '2022'
    CartPage().account_cvc = '123'


@when("Submit payment form")
def submit_payment_form():
    CartPage().next_payment_button.click()


@when("Finish purchase")
def finish_purchase():
    sleep(1)
    CartPage().terms_checkbox.click()
    CartPage().place_order_button.click()


@then("Order placed")
def check_order_placed():
    assert CartPage().thanks_notification.text == 'THANK YOU FOR YOUR ORDER!'
