from pytest_bdd import scenario
from .test_steps import *


@scenario(
    "features/zhaba.feature",
    "Cookie notification"
)
def test_cookie():
    pass
