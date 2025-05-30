#!/usr/bin/env python3
'''
This module is for making a corutine
that will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers.
'''

import asyncio
import random
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    A coroutine that collect 10 random
    numbers using an async comprehensing
    over async_generator, then return the
    10 random numbers.
    '''


    return [number async for number in async_generator()]
