#!/usr/bin/env python3
"""
A type-annotated function which takes list of float and int
and returns their sum in float
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    """
    takes a list as argument and returns their sum in float
    """

    result: float = 0.0
    for n in mxd_lst:
        result += n
    return result
