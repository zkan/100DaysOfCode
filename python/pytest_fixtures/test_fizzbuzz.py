import pytest

from fizzbuzz import FizzBuzz


@pytest.fixture
def fizzbuzz():
    fizzbuzz = FizzBuzz()
    return fizzbuzz


def test_number_is_divisible_by_3_should_get_fizz(fizzbuzz):
    expected = 'Fizz'
    assert fizzbuzz.say(3) == expected
    assert fizzbuzz.say(6) == expected


def test_number_is_divisible_by_5_should_get_buzz(fizzbuzz):
    expected = 'Buzz'
    assert fizzbuzz.say(5) == expected
    assert fizzbuzz.say(10) == expected


def test_number_is_divisible_by_3_and_5_should_get_fizzbuzz(fizzbuzz):
    expected = 'FizzBuzz'
    assert fizzbuzz.say(15) == expected
    assert fizzbuzz.say(30) == expected


def test_number_is_not_divisible_by_3_or_5_should_get_number(fizzbuzz):
    assert fizzbuzz.say(2) == 2
    assert fizzbuzz.say(4) == 4
