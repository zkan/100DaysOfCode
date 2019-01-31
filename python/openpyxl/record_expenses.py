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
ws1.append([date.today(), item, cost])

wb.save('expenses.xlsx')
