import random
import pytest

a = 10
def test_lianxi():
    x = random.randint(9, 11)
    print(x)
    if x == a:
        print("good")
    else:
        print("fail")
# class Test_lianxi:
#     @pytest.mark.skipif(condition=, reason="lalala")
#     def test_lianxi1(self):
#         assert 2 in a
