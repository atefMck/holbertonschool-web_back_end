#!/usr/bin/env python3

from typing import Union
import math

def to_kv (k: str, v: Union[int, float]) -> tuple:
    return (k , float(v ** 2))