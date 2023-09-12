"""This module defines the function sum_mixed_list."""
from typing import List


def sum_mixed_list(mxd_list: List[int | float]) -> float:
    """
    This function adds the float and int values in a list and returns a float.
    """
    return sum(mxd_list)
