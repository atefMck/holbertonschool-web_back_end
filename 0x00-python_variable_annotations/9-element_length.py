#!/usr/bin/env python3
""" azrfezaazdzad """


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ azrfezaazdzad """
    return [(i, len(i)) for i in lst]
