import allure
from hm_3_page_object.base_objects.pages.login_page import LoginPage
from hamcrest import assert_that, contains_string, has_length, has_items, equal_to

class TestNotAuthorizedZone:
    def test_title(self, browser):
        page = LoginPage()
        page.open()
        page.login_email = '12341@mail.ru'
        page.login_password = '1234123'
        page.login_button.click()
        assert page.wrong_credentials_alert.is_displayed() == True

