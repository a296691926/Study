import pytest


@pytest.fixture(scope="class")
def conf_test(request):
    print("初始化")