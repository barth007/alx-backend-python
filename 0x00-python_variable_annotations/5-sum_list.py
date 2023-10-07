#!/usr/bin/env python3
"""
A Type annotated function which takes a list of floats
and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    evalutes a list of floats and returns a floats
    """

    result: float = 0
    for n in input_list:
        result += n
    return result
