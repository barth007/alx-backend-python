#!/usr/bin/env python3
"""
An async coroutine that takes two arguments and spawn a function
n times
"""
from typing import List
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes a function n number of times
    return the  random list values of max_delay
    """

    lst: List[float] = []
    for i in range(n):
        task = await asyncio.create_task(wait_random(max_delay))
        lst.append(task)
    sorted_list: float = sorted(lst)
    return sorted_list
