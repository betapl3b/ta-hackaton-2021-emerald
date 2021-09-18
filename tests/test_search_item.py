from pytest_bdd import scenario
from tests.steps.common import *
from tests.steps.search import *


@scenario(
    "features/base.feature",
    "No results search item",
)
def test_no_results_search(browser):
    pass


@scenario(
    "features/base.feature",
    "Empty search item",
)
def test_empty_search_item(browser):
    pass


@scenario(
    "features/base.feature",
    "Success search item",
)
def test_success_search_item(browser):
    pass