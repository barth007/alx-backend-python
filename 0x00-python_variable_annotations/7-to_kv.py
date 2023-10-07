#!/usr/bin/env python3
"""
A type-annotated function thats takes a string and integer or float and
returns a tuple of type str and float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    evalutes a str and int or float
    and squares the int or float and returns a tuple
    of type str and float
    """
    squared_v: float = v ** 2
    tuple1: Tuple[str, float] = (k, squared_v)
    return tuple1
