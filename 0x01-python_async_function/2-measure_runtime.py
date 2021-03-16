#!/usr/bin/env python3
"""asqdsqdsqdsqdsqd"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """asqdsqdsqdsqdsqd"""
    counter_before = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    counter_after = time.perf_counter()
    return (counter_after - counter_before) / n
