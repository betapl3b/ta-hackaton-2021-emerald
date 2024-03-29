from src.helpers.browser import Browser
from src.helpers.page_urls import UrlFactory
from src.base_objects.elements.header import Header
from src.base_objects.elements.sidebar import Sidebar
from src.base_objects.elements.footer import Footer
from selenium.webdriver.common.by import By
from src.base_objects.elements.clickable_element import ClickableElement
from src.base_objects.elements.base_element import BaseElement


class BasePage:
    header = Header(by=By.CLASS_NAME, value='js-mainHeader', name='header')
    sidebar = Sidebar(by=By.CLASS_NAME, value='sidebar-menu', name='Side bar')
    footer = Footer(by=By.XPATH, value='//footer', name='footer')
    cookie_notification = BaseElement(by=By.XPATH, value='//div[@id="js-cookie-notification"]',
                                      name='Cookie notification')
    cookie_close_button = ClickableElement(by=By.XPATH, value='//button[@class="js-cookie-notification-accept close"]',
                                           name='Cookie close button')
    product_card_elem = ClickableElement(by=By.XPATH, value='//div[@class="carousel__item"]/a',
                                         name='product_item')
    product_card_elem_name = BaseElement(by=By.XPATH,
                                         value='//div[@class="carousel__item"]/a/div[@class="carousel__item--name"]',
                                         name='product_item')
    logout_button = ClickableElement(by=By.XPATH, value='//a[@href="/ucstorefront/en/logout"]',
                                     name='Logout button')

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
