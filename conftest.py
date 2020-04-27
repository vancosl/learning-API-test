import pytest
import requests

url = "http://127.0.0.1:5000"


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


@pytest.fixture()
def test_session_login_data():
    url1 = url + "/user_data"
    session_data = {"username": "test321", "password": "test123"}
    return url1, session_data

# test_login_函数的测试数据与assert数据
@pytest.fixture()
def user_new_input_data(user_new_assert_data):
    r = requests.get(user_new_assert_data)
    result = r.json()
    return result


@pytest.fixture()
def user_new_assert_data():
    test_name = "eason"
    url1 = url + "/user/" + test_name
    return url1
