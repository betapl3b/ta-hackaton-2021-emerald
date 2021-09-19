from selenium.webdriver.common.by import By

from src.base_objects.elements.base_element import BaseElement
from src.base_objects.elements.clickable_element import ClickableElement
from src.base_objects.elements.input import Input
from src.base_objects.elements.navigation_bar import NavigationBar


class Header(BaseElement):
    """
    Header class
    """
    navigation_bar = NavigationBar("//ul[contains(@class, 'nav__links--products js-offcanvas-links')]",
                                   name='navigation_bar', by=By.XPATH)

    sidebar_button = ClickableElement("//button[@class='btn js-toggle-sm-navigation']", 'sidebar_button', By.XPATH)
    login_sign_in_button = ClickableElement("//li[@class='liOffcanvas']/a", 'login', By.XPATH)
    b2c_accelerator_logo = BaseElement("//li[@class='liOffcanvas']/a", 'main_logo', By.XPATH)
    search_field = Input("//input[@id='js-site-search-input']", 'search_field', By.XPATH)
    search_button = ClickableElement("//button[@class='btn btn-link js_search_button']", 'search_button', By.XPATH)
    find_a_store_button = ClickableElement("div.nav-location > a", 'find_a_store_button', By.CSS_SELECTOR)
    order_tool_menu = ClickableElement(
        "//div[@class='yCmsComponent']//div[contains(@class, 'nav-order-tools js-nav-order-tools')]",
        'order_tool_menu',
        By.XPATH
    )
    quick_order_button = ClickableElement("//a[@title='Quick Order']", 'quick_order_button', By.XPATH)
    cart_import_order_button = ClickableElement("//a[@title='Import Saved Cart']", 'cart_import_order_button', By.XPATH)
    welcome_banner = BaseElement("li.logged_in", 'welcome_banner', By.CSS_SELECTOR)
    my_account_link = ClickableElement("li.yCmsComponent .myAccountLinksHeader", 'myacc', By.CSS_SELECTOR)
    my_wishlists_link = ClickableElement('//a[@title="My wishlists"]', 'wishlists', By.XPATH)
    sign_out_button = ClickableElement('.liOffcanvas a', 'sign_out_button', By.CSS_SELECTOR)
