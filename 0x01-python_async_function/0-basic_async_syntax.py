#!/usr/bin/env python3
"""This module defines the function wait_random."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This funtion returns the time(seconds) of delay."""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
