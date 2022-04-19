#!/usr/bin/python3

""" module of async """
import asyncio
import random


async def wait_random(max_delay: int = 0) -> float:
    """
    returns the random value generated for asyncio
    """
    randValue: float = random.uniform(0, max_delay)
    await asyncio.sleep(randValue)
    return randValue
