from simple_calculator.main import SimpleCalculator


def test_add_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5)

    assert result == 9


def test_add_three_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5, 6)

    assert result == 15


def test_add_many_numbers():
    numbers = range(100)

    calculator = SimpleCalculator()

    result = calculator.add(*numbers)

    assert result == 4950


def test_subtract_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.sub(10, 3)

    assert result == 7


def test_subtract_two_numbers_2():
    calculator = SimpleCalculator()

    result = calculator.sub(7, 3)

    assert result == 4
