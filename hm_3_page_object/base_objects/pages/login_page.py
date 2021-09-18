from hm_3_page_object.base_objects.base_page import BasePage
from hm_3_page_object.base_objects.elements.input import Input
from hm_3_page_object.base_objects.elements.clickable_element import ClickableElement
from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.base_objects.elements.checkbox import Checkbox
from hm_3_page_object.base_objects.elements.dropdown import Dropdown

from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    wrong_credentials_alert = BaseElement(by=By.CSS_SELECTOR, value='div.alert.alert-danger.alert-dismissable',
                                          name='Wrong credentials alert')
    # Sign In block
    login_email = Input(by=By.ID, value='j_username', name='Input for Sign In email ')
    login_password = Input(by=By.ID, value='j_password', name='Input for Sign In Password ')
    login_button = ClickableElement(by=By.XPATH, value='//button[contains(text(), "Log In")]', name='Login Button')
    # Forgotten passport
    forgot_passport_button = ClickableElement(by=By.CLASS_NAME,
                                              value='js-password-forgotten', name='Forgot passport Button')
    forgot_email = Input(by=By.ID, value='forgottenPwd.email', name='Forgot passport email')
    forgot_reset_passport_buttin = ClickableElement(
        by=By.XPATH, value='//button[contains(text(), "Reset Password")]', name='Reset password Button')

    # Register
    register_title = Dropdown(by=By.ID, value='register.title', name='Input for Registration Title ')
    register_first_name = Input(by=By.ID, value='register.firstName', name='Input for Registration First Name ')
    register_last_name = Input(by=By.ID, value='register.lastName', name='Input for Registration Last Name ')
    register_email = Input(by=By.ID, value='register.email', name='Input for Registration Email ')
    register_password = Input(by=By.ID, value='password', name='Input for Registration password ')
    register_confirm_password = Input(by=By.ID, value='register.checkPwd',
                                      name='Input for Registration Confirm password')
    confirm_agreements_checkbox = Checkbox(by=By.ID, value='registerChkTermsConditions',
                                           name='Checkbox for agreement confirmation')
    sample_checkbox = Checkbox(by=By.ID, value='consentForm.consentGiven1',
                               name='Checkbox for sample agreement')
    register_button = ClickableElement(by=By.XPATH, value='//button[contains(text(), "Register")]',
                                       name='Register Button')

    def login(self, email, password):
        self.login_email = email
        self.login_password = password
        self.login_button.click()

