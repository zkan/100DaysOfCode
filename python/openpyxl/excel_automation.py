from openpyxl import load_workbook


wb = load_workbook('financial_sample.xlsx')
ws1 = wb['Finances 2017']
max_row = ws1.max_row


def insert_sum():
    ws1[f'L{max_row}'] = '=SUM(L2:L10)'


if __name__ == '__main__':
    insert_sum()
    wb.save('financial_sample.xlsx')
