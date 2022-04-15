#!/usr/bin/env python3

"""Module sum float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sum of the list float"""
    sum = 0
    for i in input_list:
        sum += i
    return sum
