from pytest_bdd import scenario
from tests.steps.common import *
from tests.steps.register import *


@scenario(
    "features/base.feature",
    "Cookie notification"
)
def test_cookie(browser):
    pass


@scenario(
    "features/base.feature",
    "Authorization invalid",
    example_converters=dict(login=str, password=str)
)
def test_authorization_invalid(browser):
    pass


@scenario(
    "features/base.feature",
    "Authorization success",
)
def test_authorization_success(browser):
    pass
