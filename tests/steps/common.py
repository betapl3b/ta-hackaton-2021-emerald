from pytest_bdd import given, when, then

from hm_3_page_object.base_objects.pages.login_page import LoginPage
from hm_3_page_object.base_objects.pages.card_page import CardPage
from hm_3_page_object.base_objects.base_page import BasePage


@given("User on main page")
def go_to_main_page():
    BasePage().open()


@given("User on login page")
def go_to_login_page():
    LoginPage().open()


@when("Cookie notification")
def check_cookie_notif():
    assert BasePage().cookie_notification.is_displayed()


@when("Close notification")
def close_notification():
    BasePage().cookie_close_button.click()


@then("No notification")
def no_notification():
    assert not LoginPage().cookie_notification.is_displayed()


@when("Login")
def login(email, password):
    LoginPage().login(email, password)


@then("Login unsuccess")
def login_unsuccess():
    assert LoginPage().wrong_credentials_alert.is_displayed()


@when("Click 'Logout' button")
def click_logout():
    BasePage().logout_button.click()