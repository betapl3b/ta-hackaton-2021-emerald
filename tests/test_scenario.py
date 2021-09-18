from pytest_bdd import scenario
import pytest
from .test_steps import *


@scenario(
    "features/base.feature",
    "Cookie notification"
)
def test_cookie(browser):
    pass


@scenario(
    "features/base.feature",
    "Authorization blocked",
    example_converters=dict(login=str, password=str)
)
def test_authorization_blocked(browser):
    pass


@scenario(
    "features/product.feature",
    "Check product card"
)
def test_product_card(browser):
    pass
