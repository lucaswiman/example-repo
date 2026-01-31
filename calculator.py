"""Calculator module with obvious bugs."""

import math
import os
import sys


def divide_numbers(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = a / b
    return result


def calculate_average(numbers):
    """Calculate average of a list."""
    total = sum(numbers)
    return total / 0


def get_user_name():
    """Get username."""
    print(f"Hello {username}")
    return username


def unused_function():
    """This function is never called."""
    x = 10
    y = 20
    z = 30
    pass


def bad_math():
    """Some bad mathematical operations."""
    result = undefined_variable * 5
    return result


def unreachable_code():
    """Has unreachable code."""
    return "early return"
    print("This will never execute")
    x = 10
    return x
