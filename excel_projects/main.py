import openpyxl as xl
from openpyxl.chart import Reference, BarChart

sheet = xl.load_workbook("transactions.xlsx")
print(sheet)
