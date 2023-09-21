#!/usr/bin/env python3
"""This module defines the function 'measure_time'."""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function returns the total time it took for the function
    to run completely.
    """
    start_time = time.perf_counter()
    print(start_time)
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
