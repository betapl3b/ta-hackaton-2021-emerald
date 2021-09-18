import allure
from hm_3_page_object.base_objects.base_page import BasePage
from hm_3_page_object.base_objects.elements.input import Input
from hm_3_page_object.base_objects.elements.clickable_element import ClickableElement
from hm_3_page_object.base_objects.elements.base_element import BaseElement

from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    wrong_credentials_alert = BaseElement(by=By.CSS_SELECTOR, value='div.alert.alert-danger.alert-dismissable',
                                          name='Wrong credentials alert')
    # Sign In block
    login_email = Input(by=By.ID, value='j_username', name='Input for Sign In email ')
    login_password = Input(by=By.ID, value='j_password', name='Input for Sign In Password ')
    login_button = ClickableElement(by=By.XPATH, value='//button[contains(text(), "Log In")]', name='Login Button')

    def login(self, username, password):
        with allure.step(f"Perform login user with credentials: {username}:{password}"):
            self.user_icon.click()
            self.name_input = username
            self.pass_input = password
            self.login_button.click()
