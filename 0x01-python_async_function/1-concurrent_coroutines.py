#!/usr/bin/env python3
"""module of multiple coroutines """
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
       Args:
            max_delay: max sleep
            n: list size
       Return:
           float time rand
    """
    vals: List = []
    rand: List[float] = []
    for _ in range(n):
        vals.append(wait_random(max_delay))

    for val in asyncio.as_completed((vals)):
        delay = await val
        rand.append(delay)

    return rand
