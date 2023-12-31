#!/usr/bin/env python3

"""
The modules takes n as arguments as type as float and
returns the floor value of n
"""
import math


def floor(n: float) -> int:
    """
    evalutes the floor value of n
    and returns an integer
    args:
       n(float) = arguments
    """

    result: float = math.floor(n)
    return result
