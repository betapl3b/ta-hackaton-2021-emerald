from pytest_bdd import given, when, then

from hm_3_page_object.base_objects.pages.home_page import HomePage
from hm_3_page_object.base_objects.pages.categories_page import CategoriesPage
from hm_3_page_object.helpers.browser import Browser
from hm_3_page_object.helpers.page_urls import BASE_URL


@when("Enter searching word")
def enter_word(word):
    HomePage().search(word)


@when("Click search button")
def click_search():
    HomePage().header.search_button.click()


@then("No results message are showed")
def no_results():
    assert HomePage().nothing_found_message.is_displayed()


@then("Results are showed")
def results():
    assert CategoriesPage().products_found_text.is_displayed()

@then("Nothing happens")
def nothing_happens():
    assert Browser().driver.current_url == BASE_URL
