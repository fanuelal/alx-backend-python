#!/usr/bin/env python3
"""Annotate the below function’s"""
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return List of tuple of sequence
    """
    return [(i, len(i)) for i in lst]
