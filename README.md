# TDD in Python with pytest

[TDD in Python](https://www.thedigitalcatonline.com/blog/2020/09/10/tdd-in-python-with-pytest-part-1/)

---

# Calculator

## Requirements

The goal of the project is to write a class `SimpleCalculator` that performs calculations: addition, subtraction, multiplication, and division. Addition and multiplication shall accept multiple arguments. Division shall return a float value, and division by zero shall return the string `"inf"`. Multiplication by zero must raise a `ValueError` exception. The class will also provide a function to compute the average of an iterable like a list. This function gets two optional upper and lower thresholds and should remove from the computation the values that fall outside these boundaries.

As you can see the requirements are pretty simple, and a couple of them are definitely not "good" requirements, like the behaviour of division and multiplication. I added those requirements for the sake of example, to show how to deal with exceptions when developing in TDD.

---

# TDD Rule
- TDD rule number 1: Test first, code later
- TDD rule number 2: Add the reasonably minimum amount of code you need to pass the tests
- TDD rule number 3: You shouldn't have more than one failing test at a time
- TDD rule number 4: Write code that passes the test. Then refactor it.
- TDD rule number 5: A test should fail the first time you run it. If it doesn't, ask yourself why you are adding it.
- TDD rule number 6: Never refactor without tests.

# The Testing grid

| Flow     | Type    | Test? |
|----------|---------|-------|
| Incoming | Query   | Yes   |
| Incoming | Command | Yes   |
| Private  | Query   | Maybe |
| Private  | Command | Maybe |
| Outgoing | Query   | Mock  |
| Outgoing | Command | Mock  |

## python package version control

- use poetry

install package
> poetry add `cat requirements/test.txt`
> poetry add `cat requirements/prod.txt`
