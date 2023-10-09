#!/usr/bin/env python3
"""
An asynchronous coroutine takes an integer argument with a default value of
10 and wait for a random delay between 0 and max_delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    executes await on a randomly generated delay time
    """

    ran_num: float = random.uniform(0, max_delay)
    await asyncio.sleep(ran_num)
    return ran_num
