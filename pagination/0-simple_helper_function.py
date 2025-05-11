#!/usr/bin/env python3
'''
This module contains a function 
'''


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Calculates the start and end indices for a page of data
    '''

    start_index = (page -1) * page_size
    end_index = start_index + page_size
    tuple = (start_index, end_index)
    return tuple
