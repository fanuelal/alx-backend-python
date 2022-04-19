#!/usr/bin/env python3
""" Basic syntax await async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        Args:
            max_delay: max sleep
        Return:
            float time random
    """
    rand: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand)

    return delay
