from pytest_bdd import given, when, then

from hm_3_page_object.base_objects.pages.login_page import LoginPage


@given("Go to main page")
def go_to_article(browser):
    LoginPage().open()


@when("Cookie notification")
def check_cookie_notif(browser):
    assert LoginPage().cookie_notification.is_displayed()


@when("Close notification")
def close_notification(browser):
    LoginPage().cookie_close_button.click()


@then("No notification")
def no_notification(browser):
    assert not LoginPage().cookie_notification.is_displayed()
