import requests
import pytest

url = "http://127.0.0.1:5000"


class TestHelloWorld(object):

        def test_hello_world_code(self):
            r = requests.get(url+"/")
            result = r.json()
            print(result)
            assert result["code"] == 10201
            assert result["message"] == "Welcome to API testing"


class TestUser(object):

        def test_user(self):
            test_name = "eason"
            r = requests.get(url+"/user/"+test_name)
            result = r.json()
            assert result["code"] == 10200
            assert result["message"] == "hello, "+test_name


class TestGetUID(object):

    def test_get_uid_with_uid(self):
        uid_exist = 1
        r1 = requests.get(url+"/id/"+str(uid_exist))
        result = r1.json()
        assert result["code"] == 10200
        assert result["message"] == "success"
        assert result["data"]["id"] == 1
        assert result["data"]["name"] == "tom"
        assert result["data"]["age"] == 22

    def test_get_uid_with_no_uid(self):
        uid_does_not_exist = 2
        r2 = requests.get(url+"/id/"+str(uid_does_not_exist))
        result = r2.json()
        assert result["code"] == 10101
        assert result["message"] == "user id null"

    def test_get_uid_with_wrong_method(self):
        uid_exist = 1
        r3 = requests.post(url+"/id/"+str(uid_exist))
        result = r3.json()
        assert result["code"] == 10101
        assert result["message"] == "request method error"


class TestGetSearch(object):

    def test_get_search_with_right_method(self):
        data_list = ["selenium教程", "seleniumhq.org", "selenium环境安装"]
        url1 = url+"/search/"
        payload = {"q": "selenium"}
        r = requests.get(url1, params=payload)
        result = r.json()
        assert result["code"] == 10200
        assert result["data"] == data_list
        assert result["message"] == "success"

    def test_get_search_with_right_method_and_keyword(self):
        url1 = url+"/search/"
        payload = {"q": "selenium1"}
        r = requests.get(url1, params=payload)
        result = r.json()
        print(result)
        assert result["code"] == 10200
        assert result["data"] == []
        assert result["message"] == "success"

    def test_get_search_with_wrong_method(self):
        url1 = url+"/search/"
        payload = {"q": "selenium1"}
        r = requests.post(url1, params=payload)
        result = r.json()
        print(result)
        assert result["code"] == 10101
        assert result["message"] == "request method error"

def test_open():
    r = requests.get(url)
    result = r.json()
    print(result)
    assert result["code"] == 1020


def test_get_with_name(test_name):
    name = test_name["e"]
    print(name)
    r = requests.get(url+"/user/"+name)
    result = r.json()
    assert result["code"] == 1020


def test_get_with_uid():
    uid = "1"
    r = requests.get(url+"/user/"+uid)
    result = r.json()
    print(result)


def test_get_with_params():
    payload = {"q": "selenium"}
    r = requests.get(url+"/search/",params=payload)
    result = r.text
    print(result)


def test_post_with_params_json():
    payload = {"name": "jack", "age": 22, "height": 177}
    r = requests.post(url+"/add_user",json=payload)
    result = r.json()
    print(result)


def test_post_with_params_data():
    payload = {"username" : "admin", "password":"a123456"}
    r = requests.post(url+"/login",data = payload)
    result = r.json()
    print(result)


def test_upload_file():
    files = {'file': open('D:\\Test\\uploads\\log.txt','rb')}
    r = requests.post(url+"/upload",files=files)
    result = r.json()
    print(result)


def test_put():
    data = {"name":"华为手机", "price": "3999"}
    r = requests.put(url+"/phone/1",data=data)
    result = r.json()
    print(result)


def test_get_phone():
    r = requests.get(url+"/phone/1")
    result = r.json()
    print(result)


def test_login_with_session():
    s = requests.Session()
    data={"username":"jack","password":"123"}
    r = s.post(url+"/user_login",data=data)
    result = r.json()
    r2 = s.get(url+"/user_data")
    result2 = r2.json()
    print(result)
    print(result2)


def test_get_eventid():
    r = requests.get(url+"/get_activity")
    result = r.json()
    activity_id = result["data"]["id"]
    r = requests.get(url+"/get_user")
    result = r.json()
    user_id = result["data"]["id"]
    print(user_id)







