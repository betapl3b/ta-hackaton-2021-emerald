from pytest_bdd import scenario
import pytest
from .test_steps import *


@scenario(
    "features/zhaba.feature",
    "Cookie notification"
)
def test_cookie():
    pass


@scenario(
    "features/zhaba.feature",
    "Authorization blocked",
    example_converters=dict(login=str, password=str)
)
def test_authorization_blocked():
    pass
