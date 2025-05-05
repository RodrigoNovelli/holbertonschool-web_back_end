#!/usr/bin/env python3
'''
This module is for a coroutine that will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
Using the random module. 
'''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
      The coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10.
    '''

    for _ in range(10):
        await asyncio.seleep(1)
        yield random.uniform(0, 10)
