#!/usr/bin/env python3
"""Module sum of float"""
from typing import Union,List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of float and also int"""
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
