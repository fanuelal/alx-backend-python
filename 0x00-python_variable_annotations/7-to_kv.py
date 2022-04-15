#!/usr/bin/env python3
""" Module square the element"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """The second element is the square of the int/float v
    and should be annotated as a float."""

    tpl: Tuple(str, Union[int, float])
    tpl = (k, v**2)
    return tpl
