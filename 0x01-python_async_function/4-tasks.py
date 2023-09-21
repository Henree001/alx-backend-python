#!/usr/bin/env python3
"""This module defines the asynchronous coroutine 'task_wait_n'."""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function returns a sorted list of time of delay(seconds)."""
    return sorted(
        await asyncio.gather(*(task_wait_random(max_delay) for i in range(n)))
    )
