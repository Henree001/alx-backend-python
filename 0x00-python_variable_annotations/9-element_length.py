#!/usr/bin/env python3
"""This module defines the function element_length."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[str, int]]:
    """
    This function takes in an iterable and returns a list of tuples.
    """
    return [(i, len(i)) for i in lst]
