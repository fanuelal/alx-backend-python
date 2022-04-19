#!/usr/bin/env python3
"""module async comprehensing"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function generats async with comprehensing """
    return ([i async for i in async_generator()])
