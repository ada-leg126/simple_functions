import pytest
import math
import numpy as np

from simple_functions import my_sum, factorial, my_sin


class TestSimpleFunctions:
    """Tests for the functions in functions1.py."""

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4),
    ])
    def test_my_sum(self, iterable, expected):
        """my_sum adds up the items of lists and tuples."""
        assert my_sum(iterable) == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1),
        (0, 1),
    ])
    def test_factorial(self, number, expected):
        """factorial is right for small numbers, including 0! = 1."""
        assert factorial(number) == expected

    @pytest.mark.parametrize("number, expected", [
        (0.0, np.sin(0.0)),
        (math.pi / 6, np.sin(math.pi / 6)),
        (math.pi / 4, np.sin(math.pi / 4)),
        (math.pi / 2, np.sin(math.pi / 2)),
        (math.pi, np.sin(math.pi)),
        (2 * math.pi + math.pi / 4, np.sin(2 * math.pi + math.pi / 4)),
        (10 * math.pi + math.pi / 6, np.sin(10 * math.pi + math.pi / 6)),
    ])
    def test_my_sin_real_numbers(self, number, expected):
        """Compare my_sin with NumPy for real inputs."""
        assert my_sin(number) == pytest.approx(expected)

    @pytest.mark.parametrize("number, expected", [
        (1 + 2j, np.sin(1 + 2j)),
        (-1 + 0.5j, np.sin(-1 + 0.5j)),
    ])
    def test_my_sin_complex_numbers(self, number, expected):
        """Compare my_sin with NumPy for complex inputs."""
        assert my_sin(number) == pytest.approx(expected)
