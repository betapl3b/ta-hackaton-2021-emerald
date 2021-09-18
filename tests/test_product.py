from pytest_bdd import scenario
from tests.steps.common import *
from tests.steps.purchase import *

@scenario(
    "features/product.feature",
    "Check product card"
)
def test_product_card(browser):
    pass