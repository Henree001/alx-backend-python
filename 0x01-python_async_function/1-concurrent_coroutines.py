#!/usr/bin/env python3
"""This module defines the asynchronous coroutine 'wait_n'."""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This function returns a sorted list of time of delay(seconds)."""
    delay = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(delay)
