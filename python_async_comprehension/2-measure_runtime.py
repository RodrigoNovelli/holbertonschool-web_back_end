#!/usr/bin/env python3
'''
This module is for a function
that mesures the total runetime of
exe3cuting async_comprehension.
'''
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_reuntime() -> float:
    '''
    measure the total runetime of
    executing async_comprehension
    '''


    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time