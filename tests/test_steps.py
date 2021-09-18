from pytest_bdd import given, when, then


@given("Go to main page")
def go_to_article(driver):
    driver.get(url='https://apparel-uk.local:9002/ucstorefront/en')


@when("Cookie notification")
def check_cookie_notif(driver):
    assert driver.find_element_by_xpath('//div[@id="js-cookie-notification"]').is_displayed()


@when("Close notification")
def close_notification(driver):
    driver.find_element_by_xpath('//button[@class="js-cookie-notification-accept close"]').click()


@then("No notification")
def no_notification(driver):
    assert not driver.find_element_by_xpath('//div[@id="js-cookie-notification"]').is_displayed()
