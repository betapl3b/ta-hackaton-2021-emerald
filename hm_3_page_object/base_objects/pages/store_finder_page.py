from selenium.webdriver.common.by import By

from hm_3_page_object.base_objects.base_page import BasePage
from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.base_objects.elements.clickable_element import ClickableElement
from hm_3_page_object.base_objects.elements.input import Input
from hm_3_page_object.base_objects.elements.list import List
from hm_3_page_object.helpers.browser import Browser


class StoreFinderPage(BasePage):
    # Error message
    error_message = BaseElement(
        by=By.CLASS_NAME,
        value='js-storefinder-alert.alert.alert-danger.alert-dismissable.getAccAlert',
        name='Error message',
    )

    # Search input group
    query_input = Input(by=By.ID, value='storelocator-query', name='Query field')
    magnifier_button = ClickableElement(by=By.CLASS_NAME, value='btn.btn-primary', name='Search button')
    find_nearest_stores_button = ClickableElement(by=By.ID, value='findStoresNearMe', name='Find nearest stores button')

    # Search results group
    pager_from_top = BaseElement(
        by=By.XPATH,
        value="(//span[@class='js-store-finder-pager-item-from'])[1]",
        name='Top pager \'from\' value',
    )
    pager_to_top = BaseElement(
        by=By.XPATH,
        value="(//span[@class='js-store-finder-pager-item-to'])[1]",
        name='Top pager \'to\' value',
    )
    pager_all_top = BaseElement(
        by=By.XPATH,
        value="(//span[@class='js-store-finder-pager-item-all'])[1]",
        name='Top pager \'all\' value',
    )

    # Top paging buttons
    previous_button_top = ClickableElement(
        by=By.XPATH,
        value="(//button[@class='btn.btn-default.js-store-finder-pager-prev'])[1]",
        name='Top Previous button',
    )
    next_button_top = ClickableElement(
        by=By.XPATH,
        value="(//button[@class='btn.btn-default.js-store-finder-pager-next'])[1]",
        name='Top Next button',
    )

    # browser = Browser()
    # stores_list = browser.get_element(
    #     selector_type=By.CLASS_NAME,
    #     selector='store__finder--navigation-list.js-store-finder-navigation-list',
    #     timeout=5,
    # )
    stores_list = List(
        by=By.CLASS_NAME,
        value='store__finder--navigation-list.js-store-finder-navigation-list',
        name='Stores list',
    )

    # Store details block
    store_image = BaseElement(
        by=By.CLASS_NAME,
        value='div.store__finder--details-image.js-store-image',
        name='Store image',
    )
    store_name = BaseElement(by=By.CLASS_NAME, value='div.info__name.js-store-name', name='Store name')
    store_address = BaseElement(by=By.CLASS_NAME, value='div.info__address', name='Store address')
    map = BaseElement(by=By.CLASS_NAME, value='div#store__finder--map.js-store-finder-map', name='Map')
    store_openings = BaseElement(by=By.CLASS_NAME, value='dl.dl-horizontal.js-store-openings', name='Store openings')
    store_features = List(by=By.CLASS_NAME, value='ul.js-store-features', name='Store features')
    pager_from_bottom = BaseElement(
        by=By.XPATH,
        value="(//span[@class='js-store-finder-pager-item-from'])[2]",
        name='Bottom pager \'from\' value',
    )
    pager_to_bottom = BaseElement(
        by=By.XPATH,
        value="(//span[@class='js-store-finder-pager-item-to'])[2]",
        name='Bottom pager \'to\' value',
    )
    pager_all_bottom = BaseElement(
        by=By.XPATH,
        value="(//span[@class='js-store-finder-pager-item-all'])[2]",
        name='Bottom pager \'all\' value',
    )

    # Bottom paging buttons
    previous_button_bottom = ClickableElement(
        by=By.XPATH,
        value="(//button[@class='btn.btn-default.js-store-finder-pager-prev'])[2]",
        name='Top Previous button',
    )
    next_button_bottom = ClickableElement(
        by=By.XPATH,
        value="(//button[@class='btn.btn-default.js-store-finder-pager-next'])[2]",
        name='Top Next button',
    )
