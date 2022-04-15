#!/usr/bin/env python3
"""Module multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier"""
    def mul(f: float) -> float:
        """ get the second arg """
        return float(f * multiplier)
    return mul
