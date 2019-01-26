import pyperclip


AFFILIATE_CODE = '&tag=pyb0f-20'

url = pyperclip.paste()

if 'amazon' not in url:
    print('Sorry, invalid link')
else:
    new_link = f'{url}{AFFILIATE_CODE}'
    pyperclip.copy(new_link)
    print(f'Affiliate link generated and copied to clipboard')
