import random


class Roll(object):
    def __init__(self, name):
        self.name = name

    def can_defeat(self, roll):
        if (self.name == 'Rock' and roll.name == 'Scissors' or
                self.name == 'Paper' and roll.name == 'Rock' or
                self.name == 'Scissors' and roll.name == 'Paper'):
            return 'win'
        elif self.name == roll.name:
            return 'tie'
        else:
            return 'lose'


class Player(object):
    def __init__(self, name):
        self.name = name


def build_the_three_rolls():
    return [Roll('Rock'), Roll('Paper'), Roll('Scissors')]


def print_header():
    print('---------------------------------------------')
    print('            Rock, Paper, Scissors')
    print('---------------------------------------------')


def get_players_name():
    return input('What is your name? ')


def choose_roll(rolls):
    choice = input('[R]ock, [P]aper, or [S]cissors? ')
    if choice == 'R':
        return rolls[0]
    elif choice == 'P':
        return rolls[1]
    else:
        return rolls[2]


def game_loop(player1, player2, rolls):
    count = 0
    p1_wins = 0
    p2_wins = 0
    while count < 3:
        p2_roll = random.choice(rolls)
        p1_roll = choose_roll(rolls)

        outcome = p1_roll.can_defeat(p2_roll)

        print(f'{player1.name} threw {p1_roll.name}')
        print(f'{player2.name} threw {p2_roll.name}')

        if outcome == 'win':
            p1_wins += 1
        elif outcome == 'lose':
            p2_wins += 1

        count += 1

    print()
    print('----- Results -----')
    if p1_wins > p2_wins:
        print(f'{player1.name} wins!')
    elif p2_wins > p1_wins:
        print(f'{player2.name} wins!')
    else:
        print('Tie!')


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player('computer')

    game_loop(player1, player2, rolls)


if __name__ == '__main__':
    main()
