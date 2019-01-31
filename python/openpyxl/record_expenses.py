from datetime import date

from openpyxl import load_workbook, Workbook


try:
    wb = load_workbook('expenses.xlsx')
    ws1 = wb['2019']
except FileNotFoundError:
    wb = Workbook()
    ws1 = wb.create_sheet('2019')

item = input('What do you buy? ')
cost = input('How much? ')
ws1.append([date.today(), item, float(cost)])
max_row = ws1.max_row

ws1[f'D1'] = f'=SUM(C1:C{max_row})'

wb.save('expenses.xlsx')
