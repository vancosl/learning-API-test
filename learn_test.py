import requests
import pytest

url = "http://127.0.0.1:5000"

def test_open():
    r = requests.get(url)
    result = r.json()
    return result

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







