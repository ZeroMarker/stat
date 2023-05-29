from openpyxl import workbook, load_workbook

wb = load_workbook("../../dataset/GDP.xlsx")
ws = wb.active
print(ws)
