import pytest
import xlrd
def read_excel():
    # 打开文件
    para = []
    workBook = xlrd.open_workbook('F:\\data1.xls')
    sheet1 = workBook.sheet_by_index(0)  # sheet索引从0开始
    cols = sheet1.col_values(0)
    for i in cols:
        para.append(int(i))
    return para


@pytest.fixture(params=read_excel())
def add(request):
    return request.param



class Test_01:
    def test_lianxi(self, add, conf_test):
        assert add in [1, 2, 3, 4]


class Test_02:
    def test_lianxi1(self, add, conf_test):
        assert add in [1, 2, 3, 4]

if __name__ == '__main__':
    read_excel()