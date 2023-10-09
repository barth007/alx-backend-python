#!/usr/bin/env python3
"""
A function that takes integers n and max_delay
evaluates the time taken for a program to execute
"""


import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    evaluates the time taken for a program to execute
    """

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time: float = (end_time - start_time) / n
    return total_time
