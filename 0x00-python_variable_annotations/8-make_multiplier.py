#!/usr/bin/env python3
"""
A type annotated function that takes a float as argument and
return a function that multiplies a float by the argument
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    evalutes the multiplication of an argument to return a
    function
    """

    def multiply(y: float) -> float:
        """
        takes an argument and multiply it with the muliplier
        """

        return multiplier * y

    return multiply
