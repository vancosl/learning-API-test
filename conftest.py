import pytest

@pytest.fixture(scope='function')
def test_name():
    name={"e":"eason", "b":"bason" , "c": "cason"}
    return name