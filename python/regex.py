import re


phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

text = 'Alice, my phone number is 415-730-0000. Call me when it is convenient.'
mo = phone_regex.search(text)
print(mo.group())

text = 'Alice, my phone number is 415-730-0000 or 423-568-1111. Just call me.'
phones = phone_regex.findall(text)
print(phones)

phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')

text = 'Alice, my phone number is 415-730-0000. Call me when it is convenient.'
mo = phone_regex.search(text)
print(mo.group())

text = 'Alice, my phone number is 415-730-0000 or 423-568-1111. Just call me.'
phones = phone_regex.findall(text)
print(phones)

text = 'Hello World!'
mo = re.search(r'[aeiouAEIOU]\S+', text)
print(mo.group())

text = 'I have a 1,234,567,890 year old egg.'
mo = re.search(r'\d{1,3}(,\d{3})*', text)
print(mo.group())
