from pytest_bdd import scenario
from tests.steps.register import *


@scenario(
    "features/register.feature",
    "User sign up"
)
def test_register(browser):
    pass
