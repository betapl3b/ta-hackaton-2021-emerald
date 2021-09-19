import os

import pytest

from selenium import webdriver
from hm_3_page_object.helpers.browser import Browser
from selenium.webdriver.chrome.options import Options

from hm_3_page_object.helpers.logger import Logger
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    return Browser()


def pytest_addoption(parser):
    parser.addoption('--thread-number', action='store', type=int, default=0,
                     help='Number of the thread for parallel run')
    parser.addoption('--threads-count', action='store', type=int, default=1,
                     help='Count of threads for parallel run')
    parser.addoption('--test-group', action='store', type=str, default=False,
                     help='Name of test group for selective test run')


def pytest_runtest_call():
    chrome_options = Options()
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')

    if os.environ.get('JENKINS_URL') is not None:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')

    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    driver.set_window_size(1920, 1080)
    browser = Browser()
    browser.set_driver(driver)


def pytest_runtest_teardown():
    # Закрываем браузер сразу после завершения теста
    try:
        Browser().close()
    except Exception as e:
        raise (f'Не удалось закрыть браузер: {e}')


def pytest_exception_interact():
    browser = Browser()


def pytest_collection_modifyitems(session, config, items):
    Logger(f'logs/log_{config.getoption("--thread-number")}.log').debug(
        f'Thread {config.getoption("--thread-number")} has been created')
    if config.getoption("--threads-count") != 1:
        if config.getoption("--thread-number") != 0:
            # Drop not_parallel tests for multithreading test run
            items_parallel = [item for item in items if not item.get_closest_marker('not_parallel')]
            items[:] = items_parallel[
                       config.getoption("--thread-number") - 1::config.getoption("--threads-count") - 1]
        else:

            items[:] = [item for item in items if item.get_closest_marker('not_parallel')]
            Logger().debug(f'Thread #0 reserved for not_parallel tests')

    if config.getoption("--test-group"):
        items[:] = [item for item in items if item.get_closest_marker(config.getoption("--test-group"))]


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


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    Logger(filename='result.log').info(f'Step {step} succeed')
