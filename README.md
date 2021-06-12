# TDD in Python with pytest

[TDD in Python](https://www.thedigitalcatonline.com/blog/2020/09/10/tdd-in-python-with-pytest-part-1/)

---

# Calculator

## Requirements

The goal of the project is to write a class `SimpleCalculator` that performs calculations: addition, subtraction, multiplication, and division. Addition and multiplication shall accept multiple arguments. Division shall return a float value, and division by zero shall return the string `"inf"`. Multiplication by zero must raise a `ValueError` exception. The class will also provide a function to compute the average of an iterable like a list. This function gets two optional upper and lower thresholds and should remove from the computation the values that fall outside these boundaries.

As you can see the requirements are pretty simple, and a couple of them are definitely not "good" requirements, like the behaviour of division and multiplication. I added those requirements for the sake of example, to show how to deal with exceptions when developing in TDD.

---

## python package version control

- use poetry

install package
> poetry add `cat requirements/test.txt`
> poetry add `cat requirements/prod.txt`
