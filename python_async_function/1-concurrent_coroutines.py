#!/usr/bin/env python3
'''
This module is for making an async routine called wait_n
that takes in 2 int arguments (in this order): n and max_delay.
And spawns wait_random n times with the specified max_delay.
wait_n return the list of all the delays
'''


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    '''
    This function makes an async routine called wait_n
    that takes in 2 int arguments (in this order): n and max_delay.
    And spawns wait_random n times with the specified max_delay.
    wait_n return the list of all the delays
    '''
    tasks = []
    for a in range(n):
        tasks.append(wait_random(max_delay))
    list = await asyncio.gather(*tasks)
    return sorted(list)
