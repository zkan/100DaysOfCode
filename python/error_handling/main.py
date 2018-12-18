import requests


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


try:
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(response.json())
except requests.exceptions.ConnectionError as e:
    print(e)

try:
    1 / 0
except ZeroDivisionError as e:
    print(e)
finally:
    print('executing finally clause')
