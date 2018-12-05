def main():
    print_header()

    # rolls = build_the_three_rolls()

    name = get_players_name()
    print(f'Hi, {name}')

    # player1 = Player(name)
    # player2 = Player('computer')

#    game_loop(player1, player2, rolls)


def print_header():
    print('---------------------------------------------')
    print('            Rock, Paper, Scissors')
    print('---------------------------------------------')


def get_players_name():
    return input('What is your name? ')


if __name__ == '__main__':
    main()
