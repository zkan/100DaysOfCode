from collections import (
    Counter,
    ChainMap,
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

person = defaultdict(str)
print(f"Person name is {person['name']}..")


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


# ChainMap
c = ChainMap()
print(c)
d = c.new_child()
print(d)

d['name'] = 'Kan'
d['company'] = 'Pronto Tools'
print(d)
print(d.parents)
print(d.maps)
c['country'] = 'Thailand'
print(c)
print(d)

# ChainMap - ChainMap structure is "layered"
# https://stackoverflow.com/questions/23392976/what-is-the-purpose-of-collections-chainmap
x = {'a': 1, 'b': 2}
y = {'b': 10, 'c': 11}
z = ChainMap(y, x)
print(z)
print(z['b'])
