import random


options = 'red yellow blue white black green purple'.split()


def create_select_options_gen(options=options):
    for option in options:
        yield f'<option value={option}>{option.title()}</option>'


print(list(create_select_options_gen(options)))

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

new_names = [each.title() for each in NAMES]
print(new_names)

reversed_first_and_last = [f'{each.split()[1]} {each.split()[0]}' for each in NAMES]
print(reversed_first_and_last)


def gen_pairs():
    first_names = [name.split()[0].title() for name in NAMES]
    while True:
        first, second = random.sample(first_names, 2)
        if first == second:
            continue

        yield f'{first} teams up with {second}'


pairs = gen_pairs()
for _ in range(10):
    print(next(pairs))
