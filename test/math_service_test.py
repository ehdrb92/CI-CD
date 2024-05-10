import os
import sys


import pytest


sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from math_service import MathService


math_service = MathService()


def test_factorial_normal():
    assert math_service.factorial(5) == 120
    assert math_service.factorial(3) == 6


def test_factorial_zero():
    assert math_service.factorial(0) == 1


def test_factorial_negative():
    with pytest.raises(ValueError):
        math_service.factorial(-1)


def test_factorial_non_integer():
    with pytest.raises(TypeError):
        math_service.factorial("string")
