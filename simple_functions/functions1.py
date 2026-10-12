from functools import cache
from math import pi

__all__ = ['my_sum', 'factorial', 'my_sin']


def my_sum(iterable):
    """Return the sum of the items in iterable."""
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    """Return n! (n factorial) for a non-negative integer n."""
    return n * factorial(n-1) if n else 1


def my_sin(number, terms=13):
    """Approximate sine using Taylor's series.

    Real inputs are reduced to the interval [-pi, pi]. Complex inputs
    are evaluated directly because complex numbers do not support modulo.
    """
    if isinstance(number, (int, float)):
        number = ((number + pi) % (2 * pi)) - pi

    result = 0
    for n in range(terms):
        power = 2 * n + 1
        result += ((-1) ** n) * (number ** power) / factorial(power)

    return result
