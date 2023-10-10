#!/usr/bin/env python3
"""
A coroutine that execute async_commprehension 4 times
using async.gather() and measures the execution time
returns time_taken
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures the runtime of async_comprehension
    """

    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = asyncio.get_event_loop().time()
    time_taken: float = end_time - start_time
    return time_taken
