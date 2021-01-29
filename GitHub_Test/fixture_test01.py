import pytest
import allure

@pytest.fixture()
def init_xx():
    print("......初始化测试数据工作")
    with open("D:\\Study\\APP\\GitHub_Test\\data.txt", "w") as f:
        f.write('1')


class Test_xx:
    # 参数引用
    @pytest.allure.step("我是步骤一")
    def test_xx(self, init_xx):
        with open("D:\\Study\\APP\\GitHub_Test\\data.txt", 'r') as f:
            assert f.read() == '1'


@pytest.mark.parametrize("a", [1, 2, 3])   # 放到此处,类Test_oo里面的函数都可以引用参数:"a"
class Test_oo:
    # 参数引用
    @pytest.allure.step("我是步骤二")
    # @allure.severity(allure.severity_level.BLOCKER)
    def test_oo2(self, a):
            allure.attach(a, "不等于1")
            assert a != 1

    @pytest.allure.step("我是步骤三")
    def test_oo3(self, a):
            allure.attach(a, "不等于2")
            assert a != 2

    @pytest.allure.step("我是步骤四")
    def test_oo4(self, a):
            allure.attach(a, "不等于3")
            assert a != 3

    @pytest.allure.step("我是步骤五")
    def test_oo5(self, a):
        allure.attach(a, "不等于3")
        assert a != 3


if __name__ == '__main__':
    pytest.main(["-s", "fixture_test01.py"])

