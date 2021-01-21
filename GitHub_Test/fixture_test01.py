import pytest

@pytest.fixture()
def init_xx():
    print("......初始化测试数据工作")
    with open("D:\Study\APP\GitHub_Test\data.txt", "w") as f:
        f.write('1')


class Test_xx:
    # 参数引用
    def test_xx(self, init_xx):
        with open("D:\Study\APP\GitHub_Test\data.txt", 'r') as f:
            assert f.read() == '1'

class Test_oo:
    # 参数引用
    def test_oo(self, init_xx):
        with open("D:\Study\APP\GitHub_Test\data.txt", 'r') as f:
            assert f.read() == '1'


if __name__ == '__main__':
    pytest.main(["-s", "fixture_test01.py"])
