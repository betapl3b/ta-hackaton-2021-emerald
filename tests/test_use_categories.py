from pytest_bdd import scenario
from tests.steps.common import *
from tests.steps.categories import *


@scenario(
    "features/categories.feature",
    "Select categories",
)
def test_select_categories(browser):
    pass