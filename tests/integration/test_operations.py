import math
import pytest

from app.operations import (
    add,
    subtract,
    multiply,
    divide,
    exponentiate,
    modulus,
    square_root,
    logarithm,
    add_multiple,
    multiply_multiple,
)

# -------------------------------------------------------------------
# Basic arithmetic (happy paths)
# -------------------------------------------------------------------

def test_add():
    assert add(2, 3) == 5
    assert add(2.5, 3) == 5.5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(5.5, 2) == 3.5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(2.5, 4) == 10.0

# -------------------------------------------------------------------
# Division
# -------------------------------------------------------------------

def test_divide_valid():
    assert divide(6, 3) == 2.0
    assert divide(5.5, 2) == 2.75

def test_divide_by_zero():
    with pytest.raises(ValueError, match="divide by zero"):
        divide(5, 0)

# -------------------------------------------------------------------
# Exponentiation
# -------------------------------------------------------------------

def test_exponentiate_valid():
    assert exponentiate(2, 3) == 8
    assert exponentiate(5, 2) == 25
    assert exponentiate(10, -2) == 0.01

def test_exponentiate_overflow():
    # Forces OverflowError on most systems
    with pytest.raises(ValueError, match="overflow"):
        exponentiate(10.0, 10_000)

# -------------------------------------------------------------------
# Modulus
# -------------------------------------------------------------------

def test_modulus_valid():
    assert modulus(10, 3) == 1
    assert modulus(7.5, 2) == 1.5

def test_modulus_by_zero():
    with pytest.raises(ValueError, match="modulus with zero"):
        modulus(10, 0)

# -------------------------------------------------------------------
# Square Root
# -------------------------------------------------------------------

def test_square_root_valid():
    assert square_root(16) == 4.0
    assert square_root(25) == 5.0
    assert square_root(2) == math.sqrt(2)

def test_square_root_negative():
    with pytest.raises(ValueError, match="negative"):
        square_root(-4)

# -------------------------------------------------------------------
# Logarithm
# -------------------------------------------------------------------

def test_logarithm_valid():
    assert logarithm(100, 10) == 2.0
    assert logarithm(8, 2) == 3.0
    assert logarithm(math.e) == 1.0  # natural log

def test_logarithm_value_not_positive():
    with pytest.raises(ValueError, match="value must be positive"):
        logarithm(0, 10)

def test_logarithm_invalid_base():
    with pytest.raises(ValueError, match="base must be positive"):
        logarithm(100, 1)

# -------------------------------------------------------------------
# add_multiple
# -------------------------------------------------------------------

def test_add_multiple_valid():
    assert add_multiple(1, 2, 3, 4) == 10
    assert add_multiple(1.5, 2.5, 3) == 7.0

def test_add_multiple_not_enough_args():
    with pytest.raises(ValueError, match="At least two numbers"):
        add_multiple(1)

# -------------------------------------------------------------------
# multiply_multiple
# -------------------------------------------------------------------

def test_multiply_multiple_valid():
    assert multiply_multiple(2, 3, 4) == 24
    assert multiply_multiple(1.5, 2, 3) == 9.0

def test_multiply_multiple_not_enough_args():
    with pytest.raises(ValueError, match="At least two numbers"):
        multiply_multiple(5)
