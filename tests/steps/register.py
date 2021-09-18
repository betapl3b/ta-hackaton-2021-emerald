import time

from pytest_bdd import given, when, then

from hm_3_page_object.base_objects.pages.login_page import LoginPage
from hm_3_page_object.base_objects.base_page import BasePage


@then("Main page is opened")
def main_page_is_opened(browser):
    assert 'Homepage' in browser.driver.title


@when("Click 'SIGN IN / REGISTER' button")
def click_sign_in():
    BasePage().header.login_sign_in_button.click()


@then("Page title contains 'Login'")
def page_title_contains_login(browser):
    assert 'Login' in browser.driver.title


@when('Select title')
def select_title(title):
    LoginPage().register_title.choose_by_value(title.capitalize())


@when('Enter first name')
def enter_first_name(firstname):
    LoginPage().register_first_name = firstname


@when('Enter last name')
def enter_last_name(lastname):
    LoginPage().register_last_name = lastname


@when('Enter unique email address', target_fixture='email')
def enter_unique_email_adress():
    email = f'email_{str(int(time.time() * 100))[2:]}@emerald.com'
    LoginPage().register_email = email
    return email


@when('Enter email address')
def enter_email_adress(email):
    LoginPage().register_email = email


@when('Enter password')
def enter_password(password):
    LoginPage().register_password = password


@then('Password complexity bar is displayed')
def password_bar_displayed():
    assert LoginPage().password_bar.is_displayed()


@when('Enter password confirmation')
def enter_password_confirmation(password_confirmation):
    LoginPage().register_confirm_password = password_confirmation


@when("Check 'Terms and conditions'")
def check_terms():
    LoginPage().confirm_agreements_checkbox.click()


@then("'Register' button is active")
def register_button_is_active():
    LoginPage().register_button.is_enabled()


@when("Click 'Register' button")
def click_register_button():
    LoginPage().register_button.click()


@then("'Thank you for registering' banner is displayed")
def thank_you_registration_banner_is_displayed():
    pass


@then("Username is shown in header section")
def username_is_shown_in_header(firstname):
    banner_text = BasePage().header.welcome_banner.text
    assert firstname.upper() in banner_text, f"{firstname} != {banner_text}"
