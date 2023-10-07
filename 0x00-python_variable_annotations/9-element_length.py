#!/usr/bin/env python3
"""
Annotating a function below
"""
from typing import Iterable, Sequence, Tuple, List, Union


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function annotion with Sequence
    """

    return [(i, len(i)) for i in lst]
