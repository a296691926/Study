import pytest

@pytest.fixture(scope="class", autouse=True)
def add():
    print("初始化")
class Test_lianxi:
    def test_lianxi1(self):
        print("1")

    def test_lianxi2(self):
        print("2")

if __name__ == '__main__':
    pytest.main(["-s", "test_d.py"])