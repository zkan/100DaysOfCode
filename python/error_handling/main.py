try:
    1 + '1'
except TypeError:
    print('We cannot do the addition between integer and string')

try:
    print(x)
except NameError:
    print('We need to define the variable before use')
