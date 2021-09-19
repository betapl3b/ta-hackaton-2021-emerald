from pytest_bdd import scenario
from tests.steps.common import *
from tests.steps.purchase import *
from tests.steps.register import *


@scenario(
    "features/purchase.feature",
    "Purchase success"
)
def test_purchase_process(browser):
    pass