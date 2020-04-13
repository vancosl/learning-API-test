import pytest


@pytest.fixture(scope="module")
def sign_print():
    a = "1"
    b = "2"
    return a, b


