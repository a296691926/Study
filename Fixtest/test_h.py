import random
import pytest

a = 7
b = 6
def test_lianxi():
    if a > b:
        print("pass")
    else:
        pytest.xfail("失败")


test_lianxi()