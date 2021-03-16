#!/usr/bin/env python3
""" azrfezaazdzad """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ azrfezaazdzad """
    return lambda x: x * multiplier
