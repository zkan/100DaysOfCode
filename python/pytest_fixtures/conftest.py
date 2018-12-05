import pytest

from fizzbuzz import FizzBuzz


@pytest.fixture
def fizzbuzz():
    fizzbuzz = FizzBuzz()
    return fizzbuzz
