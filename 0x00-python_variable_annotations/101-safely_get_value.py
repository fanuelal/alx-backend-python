#!/usr/bin/env python3
""" Module annotations to the function"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
      -> Union[Any, T]:
    """ return Any or T format"""
    if key in dct:
        return dct[key]
    else:
        return default
