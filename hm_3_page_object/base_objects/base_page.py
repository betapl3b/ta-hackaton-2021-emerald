from hm_3_page_object.helpers.browser import Browser
from hm_3_page_object.helpers.page_urls import UrlFactory
from hm_3_page_object.base_objects.elements.header import Header
from hm_3_page_object.base_objects.elements.sidebar import Sidebar
from hm_3_page_object.base_objects.elements.footer import Footer
from selenium.webdriver.common.by import By


class BasePage:
    header = Header(by=By.CLASS_NAME, value='m-l8', name='header')
    sidebar = Sidebar(by=By.CLASS_NAME, value='sidebar-menu', name='Side bar')
    footer = Footer(by=By.XPATH, value='//footer', name='footer')

    def __init__(self):
        self._url = UrlFactory.get_url(self)

    @property
    def _browser(self):
        return Browser()

    def open(self):
        self._browser.open(self._url)
        return self

    @property
    def title(self):
        return self._browser.driver.title

    @property
    def iframes(self):
        return self._browser.get_elements(selector_type=By.TAG_NAME, selector='iframe')
