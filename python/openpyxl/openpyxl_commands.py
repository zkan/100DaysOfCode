from openpyxl import load_workbook


wb = load_workbook('financial_sample.xlsx')

print(wb.sheetnames)

# Select the last active worksheet (last sheet we edited)
# if we have more than one worksheets
ws1 = wb.active

ws2 = wb['Yearly Totals']
print(ws2)

ws1 = wb['Finances 2017']
print(ws1)

print(ws1['C9'].value)
print(ws1['B9'].value)

profit_total = 0
for index, row in enumerate(ws1['L']):
    if index == 0:
        continue

    if index == 100:
        break

    profit_total += float(row.value)

print(profit_total)

print(f'The highest cell is: {ws1.max_row}')
