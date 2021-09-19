from time import sleep

from pytest_bdd import given, then, when

from src.base_objects.base_page import BasePage
from src.base_objects.pages.login_page import LoginPage
from src.base_objects.pages.store_finder_page import StoreFinderPage


@given("User on main page")
def go_to_main_page():
    BasePage().open()


@given("User on login page")
def go_to_login_page():
    LoginPage().open()


@given("User on store finder page")
def go_to_store_finder_page():
    StoreFinderPage().open()


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


@when("'Find stores' button clicked")
def click_find_stores_button():
    sleep(1)
    StoreFinderPage().find_nearest_stores_button.click()


@when("'Magnifier' button clicked")
def click_magnifier_button():
    StoreFinderPage().magnifier_button.click()


@then("stores table is shown")
def stores_table_is_shown():
    sleep(1)
    assert StoreFinderPage().stores_list.is_displayed(), "Stores list isn't shown."


@then("error is shown")
def error_is_shown(error_text):
    assert StoreFinderPage().error_message.text == error_text, f"Error message is not {error_text}."


@when("search input filled with a value")
def fill_input(store_name):
    StoreFinderPage().query_input = store_name


@then("particular store is shown")
def error_is_shown(store_name):
    rows = StoreFinderPage().stores_list.rows
    assert rows[0].split('\n')[0] == store_name, f"Store name is not {store_name}."


@when("Close notification")
def close_notification():
    BasePage().cookie_close_button.click()

@when("Refresh browser")
def refresh_browser(browser):
    browser.refresh()
