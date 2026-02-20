"""
Recursion examples (cleaned and renamed).

Contains:
- fibonacci(n): classic recursive Fibonacci (1-indexed, like original)
- compare_numbers(a, b): returns the larger (like the original 'test' intent)
"""

from __future__ import annotations


def fibonacci(n: int) -> int:
    """Return F(n) with F(1)=F(2)=1."""
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def compare_numbers(a, b):
    """Return the greater of a and b."""
    return a if a > b else b


# Deprecated names (kept so old code keeps running)
fib = fibonacci
test = compare_numbers
