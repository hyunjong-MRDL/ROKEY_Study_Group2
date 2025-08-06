from openpyxl import Workbook
from openpyxl import load_workbook
import openpyxl

path = r'sample_folder\new_folder\data.xlsx'
wb = load_workbook(path)
sheet = wb.active
sheet['A1']='두산로보틱스 로키 화이팅'
wb.save(path)
print(sheet['A1'].value)