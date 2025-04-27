#!/usr/bin/env python3
'''
This module contains a measure_time function
with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay)
and returns total_time / n. This function returns a float
'''


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Function that returns the total time
    execution for wait_n
    '''
    timeI = time.time()
    asyncio.run(wait_n(n, max_delay))
    timeF = time.time()
    total = (timeF - timeI) / n
    return total
