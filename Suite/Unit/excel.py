import xlrd
import Function.Base

path = Function.Base.get_path()
path = path + "\\Data\LoginDate.xlsx"

myWorkbook = xlrd.open_workbook(path)
print("sheet打开", path)

table1 = myWorkbook.sheets()[0]
print("table1", table1)

print("table1.nrows", table1.nrows)

for i in range(0,table1.nrows-1):
    # print(i+1,table1.cell_value(int(i), 2))
    if "admin" == table1.cell_value(int(i), 2):
        print ("user", table1.cell_value(int(i), 0))
        print ("user", table1.cell_value(int(i), 1))
