#!/usr/bin/env python3
"""
A coroutine that loops 10 times and asychronically await
and then yield random number from 1 - 10
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    yield a random number while looping
    """

    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
