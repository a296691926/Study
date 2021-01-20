import pytest
import xlrd


def read_excel1():
    # 打开文件
    para1 = []
    workBook = xlrd.open_workbook('F:\\data2.xls')
    sheet1 = workBook.sheet_by_index(0)  # sheet索引从0开始
    cols1 = sheet1.col_values(0)
    for i in cols1:
        if i == "":
            break
        para1.append(int(i))
    return para1


def read_excel2():
    # 打开文件
    para2 = []
    workBook = xlrd.open_workbook('F:\\data2.xls')
    sheet1 = workBook.sheet_by_index(0)  # sheet索引从0开始
    cols2 = sheet1.col_values(1)

    for k in cols2:
        para2.append(int(k))
    return para2



class Test_lianxi:
    @pytest.mark.parametrize("add", read_excel1())
    def test_lianxi1(self, add):
        # if add in range(3):
        #     print(add)
        # else:
        #     print("超出范围")
        try:
            assert add in range(3)
            print(add)
        except:
            print(add, "超出范围")


    @pytest.mark.parametrize("add", read_excel1())
    @pytest.mark.parametrize("add1", read_excel2())
    def test_lianxi(self, add, add1):
        assert add, add1 in range(10)
        print(add, add1)

if __name__ == '__main__':
    pytest.main(["-s", "test_b.py"])