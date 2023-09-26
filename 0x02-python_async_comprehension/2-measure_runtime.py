#!/usr/bin/env python3
"""This module defines the coroutine measure_runtime."""

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """This function returns the total time of execution."""

    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end = time.time()

    total_time = end - start

    return total_time
