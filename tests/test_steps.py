from pytest_bdd import given, when, then

from hm_3_page_object.base_objects.pages.login_page import LoginPage
from hm_3_page_object.base_objects.base_page import BasePage


@given("User on main page")
def go_to_main_page(browser):
    BasePage().open()


@given("User on login page")
@given("Main page is opened")
@then("Main page is opened")
def go_to_login_page(browser):
    LoginPage().open()


@when("Cookie notification")
def check_cookie_notif(browser):
    assert BasePage().cookie_notification.is_displayed()


@when("Close notification")
def close_notification(browser):
    BasePage().cookie_close_button.click()


@then("No notification")
def no_notification(browser):
    assert not LoginPage().cookie_notification.is_displayed()


@when("Login")
def login(browser, login, password):
    LoginPage().login(login, password)


@then("Login unsuccess")
def login_unsuccess(browser):
    assert LoginPage().wrong_credentials_alert.is_displayed() is True

