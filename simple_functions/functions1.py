from functools import cache

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


def my_sin(x, terms=10):
    """Approximate sin(x) using the first 10 Taylor-series terms."""
    total = 0.0

    for n in range(terms):
        power = 2 * n + 1
        term = (-1) ** n * (x ** power) / factorial(power)
        total += term

    return total

print(my_sin(0.5235987756))
print(my_sin(1.5707963268))
