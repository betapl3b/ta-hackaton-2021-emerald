from pytest_bdd import scenario
from tests.steps.common import *


# @scenario(
#     "features/store_finder.feature",
#     "Show all stores",
# )
# def test_show_all_stores(browser):
#     pass


@scenario(
    "features/store_finder.feature",
    "Empty search input",
)
def test_empty_search_input(browser):
    pass


@scenario(
    "features/store_finder.feature",
    "Particular store search",
)
def test_particular_store_search(browser):
    """This test fails because store finder filter doesn't work."""

    pass
