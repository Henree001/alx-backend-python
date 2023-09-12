#!/usr/bin/env python3
"""This module defines the function sum_mixed_list."""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    This function adds the float and int values in a list and returns a float.
    """
    return sum(mxd_list)
