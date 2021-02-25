# Excel spread sheet is called a work book
# pip install openpyxl

import openpyxl

workbook = openpyxl.load_workbook('.\\Documents\\example.xlsx')

# Get sheet name if you don't know it
sheetName = workbook.get_sheet_names()

# This is for if you know the sheet name
sheet = workbook.get_sheet_by_name(sheetName[0])



for i in range(1, 8):
    print(i, sheet.cell(row = i, column = 2).value)