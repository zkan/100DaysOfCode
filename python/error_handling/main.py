try:
    1 + '1'
except TypeError:
    print('We cannot do the addition between integer and string')

try:
    print(x)
except NameError:
    print('We need to define the variable before use')


def get_user_input():
    user_input = input('Enter something: ')
    if not user_input:
        raise ValueError('Input cannot be empty')

    return user_input


try:
    print(get_user_input())
except ValueError as e:
    print(f'ERROR: {e}')
