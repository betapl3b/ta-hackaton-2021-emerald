from src.base_objects.base_page import BasePage
from src.base_objects.elements.base_element import BaseElement
from src.base_objects.elements.clickable_element import ClickableElement
from selenium.webdriver.common.by import By
from src.base_objects.elements.dropdown import Dropdown
from src.base_objects.elements.shop_categories_list import ShopCategoriesList
from src.base_objects.elements.categories_list import CategoriesList
from src.base_objects.elements.selected_category_list import SelectedCategoriesList
from src.base_objects.elements.product_grid import ProductGrid
from src.base_objects.elements.input import Input


class CategoriesPage(BasePage):

    sort_by = Dropdown(by=By.ID, value="sortOptions1", name='sort_by')

    shop_by_stores = Input(by=By.ID, value='user_location_query', name='shop by stores')

    find_shop_button = ClickableElement(by=By.ID, value='user_location_query_button', name='find shop')

    find_stores = ClickableElement(by=By.ID, value='findStoresNearMeAjax', name=' find stores')

    shops_list = ShopCategoriesList(by=By.XPATH, value="//div[@class='facet__results js-facet-container ']",
                                    name='shop list')

    price = CategoriesList(by=By.XPATH, value="//div[@id='product-facet']//div[@class='facet js-facet'][2]",
                           name='price')

    colour = CategoriesList(by=By.XPATH, value="//div[@id='product-facet']//div[@class='facet js-facet'][3]",
                            name='colour')

    size = CategoriesList(by=By.XPATH, value="//div[@id='product-facet']//div[@class='facet js-facet'][4]",
                          name='size')

    collection = CategoriesList(by=By.XPATH, value="//div[@id='product-facet']//div[@class='facet js-facet'][5]",
                                name='collection')

    category = CategoriesList(by=By.XPATH, value="//div[@id='product-facet']//div[@class='facet js-facet'][6]",
                              name='category')

    brand = CategoriesList(by=By.XPATH, value="//div[@id='product-facet']//div[@class='facet js-facet'][7]",
                           name='brand')

    selected_options = SelectedCategoriesList(by=By.XPATH, value="//div[@id='product-facet']//div[@class='facet js-facet'][1]",
                                              name='selected options')

    product_grid = ProductGrid(by=By.XPATH, value="//ul[@class='product__listing product__grid']", name='products grid')

    results_title = BaseElement(by=By.XPATH, value="//div[@class='results']/h1", name='your searched for..')

    products_found_text = BaseElement(by=By.XPATH, value="//div[contains(text(), 'found')]", name='products found text')



