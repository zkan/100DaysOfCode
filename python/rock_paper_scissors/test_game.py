import pytest

from game import (
    build_the_three_rolls,
    Player,
    Roll,
)


def test_player_should_have_name():
    p = Player('Kan')

    assert p.name == 'Kan'


def test_build_three_rolls_should_return_three_rolls():
    rolls = build_the_three_rolls()

    assert rolls[0].name == 'Rock'
    assert rolls[1].name == 'Paper'
    assert rolls[2].name == 'Scissors'


def test_roll_should_have_name():
    r = Roll('Rock')

    assert r.name == 'Rock'


@pytest.mark.parametrize('test_p1_roll, test_p2_roll, expected', [
    ('Rock', 'Scissors', 'win'),
    ('Paper', 'Rock', 'win'),
    ('Scissors', 'Paper', 'win'),
    ('Rock', 'Rock', 'tie'),
    ('Rock', 'Paper', 'lose'),
])
def test_roll_can_defeat(test_p1_roll, test_p2_roll, expected):
    p1_roll = Roll(test_p1_roll)
    p2_roll = Roll(test_p2_roll)

    assert p1_roll.can_defeat(p2_roll) == expected
