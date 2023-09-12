#!/usr/bin/env python3
"""This module defines the function zoom_array."""
from typing import List


def zoom_array(lst: List, factor: int = 2) -> List:
    """This function returns a list."""
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
