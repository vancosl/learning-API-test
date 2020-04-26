import pytest


@pytest.fixture()
def auth_data():
    auth_right = ("admin", "admin123")
    auth_none = None
    auth_null = ("", "")
    auth_wrong = ("admin", "admin1234")
    return auth_right, auth_none, auth_null, auth_wrong


@pytest.fixture()
def auth_assert():
    auth_right_assert = (10200, "Authorization success!")
    auth_none_assert = (10100, "Authorization None")
    auth_null_assert = (10102, "Authorization null")
    auth_wrong_assert = (10103, "Authorization fail!")
    return auth_right_assert, auth_none_assert, auth_null_assert, auth_wrong_assert



