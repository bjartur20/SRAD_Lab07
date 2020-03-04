import sample

def test_not_divisible_by_three_or_five():
    assert sample.fizz_buzz(2) == 2

def test_divisible_by_five_not_three():
    assert sample.fizz_buzz(5) == 'Fizz'

def test_divisible_by_three_not_five():
    assert sample.fizz_buzz(3) == 'Buzz'