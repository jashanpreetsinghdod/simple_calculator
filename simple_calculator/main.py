# -*- coding: utf-8 -*-

import operator
from functools import reduce

__all__ = ['SimpleCalculator']

class SimpleCalculator:
    """A very small calculator with a few arithmetic helpers."""

    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(operator.mul, args)

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float('inf')

    def avg(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count

    def square(self, x):
        """
        Return the square of *x*.

        Parameters
        ----------
        x : int or float
            The number to be squared.

        Returns
        -------
        int or float
            x multiplied by itself.

        Raises
        ------
        TypeError
            If *x* is not a numeric type.
        """
        if not isinstance(x, (int, float)):
            raise TypeError('square() expects a numeric argument')
        return x * x
