# app/operations.py

"""
Module: operations.py

This module contains comprehensive arithmetic and mathematical functions that perform
various operations including basic arithmetic (addition, subtraction, multiplication,
division) and advanced operations (exponentiation, modulus, square root, logarithm).

These functions are foundational for building complex applications such as calculators,
scientific computing tools, or financial applications.

Functions:
- add(a: Number, b: Number) -> Number: Returns the sum of a and b.
- subtract(a: Number, b: Number) -> Number: Returns the difference when b is subtracted from a.
- multiply(a: Number, b: Number) -> Number: Returns the product of a and b.
- divide(a: Number, b: Number) -> float: Returns the quotient when a is divided by b.
- exponentiate(base: Number, exponent: Number) -> Number: Returns base raised to the power of exponent.
- modulus(a: Number, b: Number) -> Number: Returns the remainder when a is divided by b.
- square_root(a: Number) -> float: Returns the square root of a.
- logarithm(value: Number, base: Number) -> float: Returns the logarithm of value with specified base.

Usage:
These functions can be imported and used in other modules or integrated into APIs
to perform mathematical operations based on user input.
"""

from typing import Union
import math

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    Add two numbers and return the result.

    Parameters:
    - a (int or float): The first number to add.
    - b (int or float): The second number to add.

    Returns:
    - int or float: The sum of a and b.

    Example:
    >>> add(2, 3)
    5
    >>> add(2.5, 3)
    5.5
    """
    result = a + b
    return result

def subtract(a: Number, b: Number) -> Number:
    """
    Subtract the second number from the first and return the result.

    Parameters:
    - a (int or float): The number from which to subtract.
    - b (int or float): The number to subtract.

    Returns:
    - int or float: The difference between a and b.

    Example:
    >>> subtract(5, 3)
    2
    >>> subtract(5.5, 2)
    3.5
    """
    result = a - b
    return result

def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers and return the product.

    Parameters:
    - a (int or float): The first number to multiply.
    - b (int or float): The second number to multiply.

    Returns:
    - int or float: The product of a and b.

    Example:
    >>> multiply(2, 3)
    6
    >>> multiply(2.5, 4)
    10.0
    """
    result = a * b
    return result

def divide(a: Number, b: Number) -> float:
    """
    Divide the first number by the second and return the quotient.

    Parameters:
    - a (int or float): The dividend.
    - b (int or float): The divisor.

    Returns:
    - float: The quotient of a divided by b.

    Raises:
    - ValueError: If b is zero, as division by zero is undefined.

    Example:
    >>> divide(6, 3)
    2.0
    >>> divide(5.5, 2)
    2.75
    >>> divide(5, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero!
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    
    result = a / b
    return result

def exponentiate(base: Number, exponent: Number) -> Number:
    """
    Raise the base to the power of the exponent and return the result.

    Parameters:
    - base (int or float): The base number.
    - exponent (int or float): The exponent to raise the base to.

    Returns:
    - int or float: The result of base raised to the power of exponent.

    Raises:
    - ValueError: If the result causes an overflow.

    Example:
    >>> exponentiate(2, 3)
    8
    >>> exponentiate(5, 2)
    25
    >>> exponentiate(2.5, 2)
    6.25
    >>> exponentiate(10, -2)
    0.01
    """
    try:
        result = base ** exponent
    except OverflowError:
        raise ValueError("Result too large (overflow)")
    
    return result

def modulus(a: Number, b: Number) -> Number:
    """
    Calculate the modulus (remainder) when a is divided by b.

    Parameters:
    - a (int or float): The dividend.
    - b (int or float): The divisor.

    Returns:
    - int or float: The remainder when a is divided by b.

    Raises:
    - ValueError: If b is zero, as modulus by zero is undefined.

    Example:
    >>> modulus(10, 3)
    1
    >>> modulus(15, 4)
    3
    >>> modulus(7.5, 2)
    1.5
    >>> modulus(10, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot perform modulus with zero!
    """
    if b == 0:
        raise ValueError("Cannot perform modulus with zero!")
    
    result = a % b
    return result

def square_root(a: Number) -> float:
    """
    Calculate and return the square root of a number.

    Parameters:
    - a (int or float): The number to calculate the square root of.

    Returns:
    - float: The square root of a.

    Raises:
    - ValueError: If a is negative, as square root of negative numbers
                  results in complex numbers (not supported here).

    Example:
    >>> square_root(16)
    4.0
    >>> square_root(25)
    5.0
    >>> square_root(2)
    1.4142135623730951
    >>> square_root(-4)
    Traceback (most recent call last):
        ...
    ValueError: Cannot calculate square root of negative number!
    """
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    
    result = math.sqrt(a)
    return result

def logarithm(value: Number, base: Number = math.e) -> float:
    """
    Calculate the logarithm of a value with a specified base.

    Parameters:
    - value (int or float): The value to calculate the logarithm of.
    - base (int or float, optional): The base of the logarithm. Defaults to e (natural log).

    Returns:
    - float: The logarithm of value with the specified base.

    Raises:
    - ValueError: If value is not positive, or if base is not positive or equals 1.

    Example:
    >>> logarithm(100, 10)
    2.0
    >>> logarithm(8, 2)
    3.0
    >>> logarithm(math.e)  # Natural logarithm
    1.0
    >>> logarithm(0, 10)
    Traceback (most recent call last):
        ...
    ValueError: Logarithm value must be positive!
    >>> logarithm(100, 1)
    Traceback (most recent call last):
        ...
    ValueError: Logarithm base must be positive and not equal to 1!
    """
    if value <= 0:
        raise ValueError("Logarithm value must be positive!")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1!")
    
    result = math.log(value, base)
    return result


# Additional utility functions for batch operations

def add_multiple(*numbers: Number) -> Number:
    """
    Add multiple numbers together.

    Parameters:
    - *numbers (int or float): Variable number of arguments to add.

    Returns:
    - int or float: The sum of all numbers.

    Raises:
    - ValueError: If fewer than 2 numbers are provided.

    Example:
    >>> add_multiple(1, 2, 3, 4)
    10
    >>> add_multiple(1.5, 2.5, 3)
    7.0
    """
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required!")
    
    return sum(numbers)

def multiply_multiple(*numbers: Number) -> Number:
    """
    Multiply multiple numbers together.

    Parameters:
    - *numbers (int or float): Variable number of arguments to multiply.

    Returns:
    - int or float: The product of all numbers.

    Raises:
    - ValueError: If fewer than 2 numbers are provided.

    Example:
    >>> multiply_multiple(2, 3, 4)
    24
    >>> multiply_multiple(1.5, 2, 3)
    9.0
    """
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required!")
    
    result = 1
    for num in numbers:
        result *= num
    
    return result