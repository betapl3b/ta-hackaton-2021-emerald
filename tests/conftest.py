import pytest

from selenium import webdriver
from hm_3_page_object.helpers.browser import Browser
from selenium.webdriver.chrome.options import Options

from hm_3_page_object.helpers.logger import Logger


@pytest.fixture
def browser():
    return Browser()


def pytest_addoption(parser):
    parser.addoption('--thread-number', action='store', type=int, default=0,
                     help='Number of the thread for parallel run')
    parser.addoption('--threads-count', action='store', type=int, default=1,
                     help='Count of threads for parallel run')


def pytest_runtest_call():
    chrome_options = Options()
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(chrome_options=chrome_options)
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
    if config.getoption("--threads-count") != 1:
        items[:] = items[config.getoption("--thread-number")::config.getoption("--threads-count")]


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
