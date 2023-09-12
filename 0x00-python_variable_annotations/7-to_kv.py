#!/usr/bin/env python3
"""This module defines the function to_kv."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function accepts a string and an int or float as its
    two arguments and returns a Tuple with first and second
    elements as string and float respectively.
    """
    return (k, float(v * v))
