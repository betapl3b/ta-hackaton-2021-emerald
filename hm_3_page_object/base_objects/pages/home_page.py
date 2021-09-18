from hm_3_page_object.base_objects.base_page import BasePage
from hm_3_page_object.base_objects.elements.clickable_element import ClickableElement
from hm_3_page_object.base_objects.elements.header import Header
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    all_href_images = ClickableElement(by=By.XPATH, value="//a//img", name='clickable_images')
    the_biggest_banner = ClickableElement(by=By.XPATH, value="//img[@title='Start Your Season']",
                                          name='start you season')
    show_now = ClickableElement(by=By.XPATH, value = "//img[@title='Save Big on Select Streetwear']",
                                name='Save Big on Select Streetwear')

    shop_women = ClickableElement(by=By.XPATH, value="//div[@class='simple-banner banner__component--responsive']//"
                                                     "img[contains(@title, 'Women')]", name='shop women')
    shop_men = ClickableElement(by=By.XPATH, value="//div[@class='simple-banner banner__component--responsive']//"
                                                   "img[contains(@title, 'Men')]", name='shop men')
    shop_teens = ClickableElement(by=By.XPATH, value="//div[@class='simple-banner banner__component--responsive']//"
                                                     "img[contains(@title, 'Youth')]", name='shop teens')
    shop_brands = ClickableElement(by=By.XPATH, value="//div[@class='simple-banner banner__component--responsive']//"
                                                      "img[contains(@title, 'Our brand range')]", name='shop brands')
    best_selling_products = ClickableElement(by=By.XPATH, value="//div[contains(text(), 'Best Selling Products')]/"
                                                                "following-sibling::div//div[@class='owl-wrapper']/div",
                                             name='Best Selling Products')
    best_selling_products_next = ClickableElement(by=By.XPATH, value="//div[contains(text(), 'Best Selling Products')]/"
                                                                     "following-sibling::div//div[@class='owl-next']",
                                                  name='next best selling product')
    best_selling_products_prv = ClickableElement(by=By.XPATH, value="//div[contains(text(), 'Best Selling Products')]/"
                                                                    "following-sibling::div//div[@class='owl-prev']",
                                                 name='previous best selling product')
    new_products = ClickableElement(by=By.XPATH, value="//div[contains(text(), \"What's New\")]/"
                                                       "following-sibling::div//div[@class='owl-wrapper']/div",
                                    name='New products')
    new_products_next = ClickableElement(by=By.XPATH, value="//div[contains(text(), \"What's New\")]/"
                                                            "following-sibling::div//div[@class='owl-next']",
                                         name='next new product')
    new_products_prev = ClickableElement(by=By.XPATH, value="//div[contains(text(), \"What's New\")]/"
                                                            "following-sibling::div//div[@class='owl-prev']",
                                         name='next new product')
    read_more = ClickableElement(by=By.XPATH, value="//img[@title='Free Shipping on All Orders This Weekend']")

    thanks_tab = ClickableElement(by=By.XPATH, value="//div[@class='alert alert-info alert-dismissable getAccAlert']")
    close_thanks_tub = ClickableElement(by=By.XPATH, value="//div[@class='alert alert-info alert-dismissable getAccAlert']"
                                                           "/button")
    header = Header()




