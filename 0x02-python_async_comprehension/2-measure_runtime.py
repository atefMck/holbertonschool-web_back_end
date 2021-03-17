#!/usr/bin/env python3
"""zdqsdlksqjksq"""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """zdqsdlksqjksq"""
    counter_before = time.perf_counter()
    coroutines = (async_comprehension() for i in range(4))
    await asyncio.gather(*coroutines)
    counter_after = time.perf_counter()
    return counter_after - counter_before
