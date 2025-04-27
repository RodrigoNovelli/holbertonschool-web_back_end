#!/usr/bin/env python3
'''
type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier.
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Function that returns a function
    '''
    def multiplier_function(x: float) -> float:
        '''
        Function that multiplies a float for a multiplier
        '''
        return x * multiplier
    return multiplier_function
