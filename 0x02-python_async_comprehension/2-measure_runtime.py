#!/usr/bin/env python3
"""module measure runtime"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """time measuring function"""
    pre_run = time.perf_counter()
    task_list = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task_list)
    final = time.perf_counter()

    return (final - pre_run)
