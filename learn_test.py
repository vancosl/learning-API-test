import requests
import pytest

url = "http://127.0.0.1:5000"


class TestHelloWorld(object):

    def test_hello_world_code(self):
        r = requests.get(url + "/")
        result = r.json()
        print(result)
        assert result["code"] == 10201
        assert result["message"] == "Welcome to API testing"


class TestUser(object):

    def test_user(self):
        test_name = "eason"
        r = requests.get(url + "/user/" + test_name)
        result = r.json()
        assert result["code"] == 10200
        assert result["message"] == "hello, " + test_name


class TestGetUID(object):

    def test_get_uid_with_uid(self):
        uid_exist = 1
        r1 = requests.get(url + "/id/" + str(uid_exist))
        result = r1.json()
        assert result["code"] == 10200
        assert result["message"] == "success"
        assert result["data"]["id"] == 1
        assert result["data"]["name"] == "tom"
        assert result["data"]["age"] == 22

    def test_get_uid_with_no_uid(self):
        uid_does_not_exist = 2
        r2 = requests.get(url + "/id/" + str(uid_does_not_exist))
        result = r2.json()
        assert result["code"] == 10101
        assert result["message"] == "user id null"

    def test_get_uid_with_wrong_method(self):
        uid_exist = 1
        r3 = requests.post(url + "/id/" + str(uid_exist))
        result = r3.json()
        assert result["code"] == 10101
        assert result["message"] == "request method error"


class TestGetSearch(object):

    def test_get_search_with_right_method(self):
        data_list = ["selenium教程", "seleniumhq.org", "selenium环境安装"]
        url1 = url + "/search/"
        payload = {"q": "selenium"}
        r = requests.get(url1, params=payload)
        result = r.json()
        assert result["code"] == 10200
        assert result["data"] == data_list
        assert result["message"] == "success"

    def test_get_search_with_right_method_and_keyword(self):
        url1 = url + "/search/"
        payload = {"q": "selenium"}
        r = requests.get(url1, params=payload)
        result = r.json()
        print(result)
        assert result["code"] == 10200
        assert result["data"] == []
        assert result["message"] == "success"

    def test_get_search_with_wrong_method(self):
        url1 = url + "/search/"
        payload = {"q": "selenium1"}
        r = requests.post(url1, params=payload)
        result = r.json()
        print(result)
        assert result["code"] == 10101
        assert result["message"] == "request method error"


class TestLoginIn(object):

    def test_login_with_post(self):
        payload = {"username": "admin", "password": "a123456"}
        r = requests.post(url + "/login", data=payload)
        result = r.json()
        assert result["code"] == 10200
        assert result["message"] == "login success"

    def test_login_with_post_wrong_params(self):
        payload_none_username = {"password": "a123456"}
        payload_none_password = {"username": "admin"}
        payload_null_username = {"username": "", "password": "a123456"}
        payload_null_password = {"username": "admin", "password": ""}
        payload_wrong_username = {"username": "admin1", "password": "a123456"}
        payload_wrong_password = {"username": "admin", "password": "a1234561"}
        r1 = requests.post(url + "/login", data=payload_none_username)
        r2 = requests.post(url + "/login", data=payload_none_password)
        result1 = r1.json()
        result2 = r2.json()
        assert result1["code"] == 10102
        assert result2["code"] == 10102
        assert result1["message"] == "username or password is None"
        assert result2["message"] == "username or password is None"
        r3 = requests.post(url + "/login", data=payload_null_username)
        r4 = requests.post(url + "/login", data=payload_null_password)
        result3 = r3.json()
        result4 = r4.json()
        assert result3["code"] == 10103
        assert result4["code"] == 10103
        assert result3["message"] == "username or password is null"
        assert result4["message"] == "username or password is null"
        r5 = requests.post(url + "/login", data=payload_wrong_username)
        r6 = requests.post(url + "/login", data=payload_wrong_password)
        result5 = r5.json()
        result6 = r6.json()
        assert result5["code"] == 10104
        assert result6["code"] == 10104
        assert result5["message"] == "username or password error"
        assert result6["message"] == "username or password error"


class TestAddUser(object):

    def test_add_user(self):
        payload = {"name": "jack", "age": 22, "height": 177}
        r = requests.post(url + "/add_user", json=payload)
        result = r.json()
        print(result)
        assert result["code"] == 10200
        assert result["message"] == "add success"
        assert result["data"] == payload

    def test_add_user_with_wrong_params_format(self):
        payload = {"name": "jack", "age": 22, "height": 177}
        r = requests.post(url + "/add_user", params=payload)
        result = r.json()
        print(result)
        assert result["code"] == 10105
        assert result["message"] == "format error"

    def test_add_user_with_null_key(self):
        payload = {"age": 22, "height": 177}
        r = requests.post(url + "/add_user", json=payload)
        result = r.json()
        print(result)
        assert result["code"] == 10102
        assert result["message"] == "key null"

    def test_add_user_with_wrong_name(self):
        payload_null_name = {"name": "", "age": 22, "height": 177}
        payload_exist_name = {"name": "tom", "age": 22, "height": 177}
        r = requests.post(url + "/add_user", json=payload_null_name)
        result = r.json()
        assert result["code"] == 10103
        assert result["message"] == "name null"
        r = requests.post(url + "/add_user", json=payload_exist_name)
        result = r.json()
        assert result["code"] == 10104

    def test_add_user_wrong_method(self):
        payload = {"name": "jack", "age": 22, "height": 177}
        r = requests.get(url + "/add_user", json=payload)
        result = r.json()
        print(result)
        assert result["code"] == 10101
        assert result["message"] == "request method error"


class TestPostHeader(object):
    def test_post_header(self):
        headers = {"Content-Type": "application/json", "token": "1234"}
        r = requests.post(url + "/header", headers=headers)
        result = r.json()
        assert result["code"] == 10200
        assert result["message"] == "header ok!"
        assert result["data"] == headers


class TestPostAuth(object):

    def test_post_auth(self, auth_data, auth_assert):
        url1 = url + "/auth"
        auth_right = auth_data[0]
        auth_none = auth_data[1]
        auth_null = auth_data[2]
        auth_wrong = auth_data[3]

        r = requests.post(url1, auth=auth_right)
        result = r.json()
        assert result["code"] == auth_assert[0][0]
        assert result["message"] == auth_assert[0][1]

        r1 = requests.post(url1, auth=auth_none)
        result = r1.json()
        assert result["code"] == auth_assert[1][0]
        assert result["message"] == auth_assert[1][1]

        r2 = requests.post(url1, auth=auth_null)
        result = r2.json()
        assert result["code"] == auth_assert[2][0]
        assert result["message"] == auth_assert[2][1]

        r3 = requests.post(url1, auth=auth_wrong)
        result = r3.json()
        assert result["code"] == auth_assert[3][0]
        assert result["message"] == auth_assert[3][1]


class TestUploadFile(object):

    def test_upload_file(self):
        url1 = url + "/upload"
        file_path = {"file": open("test.txt", "rb")}
        r = requests.post(url1, files=file_path)
        result = r.json()
        assert result["code"] == 10200
        assert result["message"] == "upload success!"


class TestMoreUsed(object):

    def test_more_used_get(self):
        pid = 1
        url1 = url + "/phone/" + str(pid)
        phone_info = {"id": 1, "name": "小米手机", "price": 1999}
        data_assert = ["code", "message", "data"]
        data_value = [10201, "get success", phone_info]
        r = requests.get(url1)
        result = r.json()
        print(result)
        assert result[data_assert[0]] == data_value[0]
        assert result[data_assert[1]] == data_value[1]
        assert result[data_assert[2]] == data_value[2]

    def test_more_used_put(self):
        pid = 1
        url1 = url + "/phone/" + str(pid)
        phone_info = {"id": 1, "name": "小米手机", "price": 1999}
        r = requests.put(url1, phone_info)
        result = r.json()
        print(result)

    def test_more_used_delete(self):
        pid = 1
        url1 = url + "/phone/" + str(pid)
        phone_info = {"id": 1, "name": "小米手机", "price": 1999}
        r = requests.delete(url1)
        result = r.json()
        print(result)
        assert result["code"] == 10203
        assert result["message"] == "delete success"


class TestSessionLogin(object):
    def test_session_login(self):
        url1 = url + "/user_login"
        session = {"username": "test321", "password": "test123"}
        r = requests.post(url1, data=session)
        result = r.json()
        print(result)
        assert result["code"] == 10200
        assert result["message"] == "login success"

    def test_session_user_data(self):
        url1 = url + "/user_data"
        session_data = {"username": "test321", "password": "test123"}
        r = requests.get(url1, params=session_data)
        result = r.json()
        print(result)
        assert result["code"] == 10200
        assert result["message"] == "hello, stranger"
