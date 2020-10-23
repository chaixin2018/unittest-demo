from openpyxl import Workbook, load_workbook

excel = "E:\\test_evidence.xlsx"
wb = load_workbook(excel)
print("111")
wb.save(excel)
print("222")