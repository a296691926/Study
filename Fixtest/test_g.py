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
        para1.append(str(int(i)))
    print(tuple(para1))
    return tuple(para1)


def read_excel2():
    # 打开文件
    para2 = []
    workBook = xlrd.open_workbook('F:\\data2.xls')
    sheet1 = workBook.sheet_by_index(0)  # sheet索引从0开始
    cols2 = sheet1.col_values(1)

    for k in cols2:
        para2.append(int(k))
    return tuple(para2)


class Test_xx:
    @pytest.mark.parametrize("a, b, new", [("1", "2", "e"), ("3", "4", "f")])
    def test_xx(self, a, b, new):
        print("a:", a)
        print("b:", b)
        print("new:", new)

    @pytest.mark.parametrize("z, x, c", [read_excel1(), read_excel2()])
    def test_oo(self, z, x, c):
        print("z:", z)
        print("x:", x)
        print("c:", c)

if __name__ == '__main__':
    pytest.main(["-s", "test_g.py"])
    read_excel1()



