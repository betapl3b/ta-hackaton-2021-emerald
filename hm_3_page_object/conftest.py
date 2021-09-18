import pytest
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from hm_3_page_object.helpers.browser import Browser
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    return Browser()


def pytest_runtest_call():
    with allure.step('Setup driver'):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Chrome(chrome_options=chrome_options)
        with allure.step('Maximize window'):
            driver.set_window_size(1920, 1080)
        browser = Browser()
        browser.set_driver(driver)


def pytest_runtest_teardown():
    # Закрываем браузер сразу после завершения теста
    try:
        Browser().close()
    except Exception as e:
        raise (f'Не удалось закрыть браузер: {e}')




@pytest.fixture(scope='function')
def soft_assert():
    """
    Soft assert
    """
    _exc = []

    def soft_assertion(assertion, *args):
        try:
            assertion(*args)
        except AssertionError as ex:
            _exc.append(f"FAILED: {str(ex)}")

    yield soft_assertion

    if _exc:
        error_text = '\n'.join(_exc)
        raise AssertionError(f'Found errors: {len(_exc)}\n'
                             f'{error_text}')
