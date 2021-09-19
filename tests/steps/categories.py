import time
from pytest_bdd import given, when, then

from hm_3_page_object.base_objects.pages.home_page import HomePage
from hm_3_page_object.base_objects.pages.categories_page import CategoriesPage


@when("Click 'shop women'")
def shop_women_click():
    HomePage().shop_women.click()

@then("User on searched for women page")
def searched_for_women():
    assert CategoriesPage().results_title.text == 'You searched for "women"'

@when("Select first shop")
def select_first_shop():
    (CategoriesPage().shops_list.list[1]).select()

@when("Search shop which starts with LONDON")
def shop_london():
    CategoriesPage().shop_by_stores.send_keys('LONDON')
    CategoriesPage().find_shop_button.click()
    time.sleep(2)

@when("Select first price")
def select_first_price():
    (CategoriesPage().price.list[0]).select()

@when("Select first colour")
def select_first_colour():
    (CategoriesPage().colour.list[0]).select()

@when("Select first size")
def select_first_colour():
    (CategoriesPage().size.list[0]).select()

@then("Collection list is not displayed")
def no_collection_list():
    assert CategoriesPage().collection.not_displayed()

@then("Category list is not displayed")
def no_category_list():
    assert CategoriesPage().category.not_displayed()

@then("Brand list is not displayed")
def no_brand_list():
    assert CategoriesPage().brand.not_displayed()

@then("1 product found")
def only_one_product_found():
    assert CategoriesPage().products_found_text.text == '1 Products found'

@then("products grid contains 1 item")
def one_item_in_produt_grid():
    assert len(CategoriesPage().product_grid.list) == 1

@then("Applied Facets is Female")
def applied_fasets_is_female():
    assert CategoriesPage().selected_options.list[0].text == 'Female '
