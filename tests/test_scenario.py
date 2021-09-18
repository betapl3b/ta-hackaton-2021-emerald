from pytest_bdd import scenario
import pytest
from .test_steps import *


@scenario(
    "features/zhaba.feature",
    "Cookie notification"
)
def test_cookie():
    pass


@pytest.mark.parametrize(
    ["login", "password"],
    [('12341@mail.ru', '1234123')],
)
@scenario(
    "features/zhaba.feature",
    "Authorization blocked",
)
def test_parametrized(login, password):
    pass
