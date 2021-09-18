from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    yield driver
    driver.quit()
