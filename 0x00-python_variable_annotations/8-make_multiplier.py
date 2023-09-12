#!/usr/bin/env python3
"""This module defines the function make_multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier.
    """

    def float_multiplier(num: float) -> float:
        return num * multiplier

    return float_multiplier
