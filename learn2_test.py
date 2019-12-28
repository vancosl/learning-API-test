import pytest

@pytest.fixture()
def testdata2():
    print("fixture start")
    yield testdata2
    print("fixture end")

#@pytest.mark.usefixtures('testdata2')
def test_data2(testdata2):
    print("working")

if __name__ == '__main__':
    pytest.main('-q learn2_test.py')