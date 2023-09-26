#!/usr/bin/env python3
"""This module defines a couroutine called async_comprehension."""
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    This function returns a list of random numbers generated from
    'async_generator'.
    """

    return [await i for i in async_generator()]
