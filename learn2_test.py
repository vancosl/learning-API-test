import pytest


def test_result(test_add):
    assert test_add == 2
    print(test_add)


@pytest.fixture()
def test_add(send_value):
    a = send_value[0]
    b = send_value[1]
    c = a + b
    return c


@pytest.fixture()
def send_value():
    a = [1, 2]
    return a


def test_sign_print(sign_print):
    print(sign_print[0])
    assert 0
