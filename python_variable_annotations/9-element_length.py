#!/usr/bin/env python3
'''
This module is to document an iterable type function
'''


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    This function returns an tuple made from
    an iterable object and an int that its
    its len.
    '''
    return [(i, len(i)) for i in lst]
