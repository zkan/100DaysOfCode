from collections import (
    Counter,
    defaultdict,
    namedtuple,
)


# defaultdict
company = {
    'name': 'Pronto Tools'
}
try:
    company['developers'].append('Kan')
except KeyError:
    print("KeyError: 'developers'")


company = defaultdict(list)
company['name'] = 'Pronto Tools'
company['engineers'].append('Kan')
company['engineers'].append('Mils')
print(company)


# Counter
file_name = 'harry.txt'

with open(file_name) as f:
    text = f.read()
    words = text.split(' ')
    c = Counter(words)
    print(f'Top 5 common words: {c.most_common(5)}')


# namedtuple
User = namedtuple('User', 'name role')
user = User(name='bob', role='coder')
print(user, user.name, user.role)
