import pytest


class Test_lianxi1:
    def test_lianxi1(self, conf_test):
        print("1")

    def test_lianxi2(self, conf_test):
        print("2")
class Test_lianxi2:
    def test_lianxi1(self, conf_test):
        print("3")

    def test_lianxi2(self, conf_test):
        print("4")


if __name__ == '__main__':
    pytest.main(["-s", "test_e.py"])