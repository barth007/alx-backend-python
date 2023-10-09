#!/usr/bin/env python3
"""
An asynchronous coroutine takes an integer argument with a default value of
10 and wait for a random delay between 0 and max_delay
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    executes await on a randomly generated delay time
    """

    ran_num = random.uniform(0, max_delay)
    await asyncio.sleep(ran_num)
    return ran_num
