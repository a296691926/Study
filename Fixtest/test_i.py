import pytest

@pytest.fixture
def add():
    return 1

# @pytest.mark.usefixtures("add")  # 拿不到返回值
class Test_lianxi:
    def test_lianxi1(self, add):  # 可以拿到返回值
        assert add == 1

    def test_lianxi2(self, add):
        assert add < 2

