from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from hm_3_page_object.helpers.logger import Logger
from hm_3_page_object.helpers.singleton import SingletonPerThread


class Browser(metaclass=SingletonPerThread):
    driver: WebDriver = None
    logger: Logger = Logger(filename='result.log')

    def set_driver(self, driver: WebDriver):
        self.driver = driver

    def close(self):
        """
        Закрыть браузер
        """
        self.driver.quit()
        self.driver = None

    def refresh(self):
        """
        Обновить страницу
        """
        self.open(url=self.driver.current_url)

    def get_element(self, selector_type, selector, timeout=1, method=EC.visibility_of_element_located):
        return WebDriverWait(self.driver, timeout=timeout).until(
            method((selector_type, selector)),
            f'Can\'t find visible element by {selector_type}:{selector}')

    def get_elements(self, selector_type, selector, timeout=1, method=EC.visibility_of_any_elements_located):
        return WebDriverWait(self.driver, timeout=timeout).until(
            method((selector_type, selector)),
            f'Can\'t find visible element by {selector_type}:{selector}')

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    def scroll_to(self, element):
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = self.driver.execute_script('return window.innerHeight')
        window_y = self.driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    def open(self, url):
        self.driver.get(url)

    @property
    def window_side(self):
        return self.driver.get_window_size()
