#!/usr/bin/env python3
"""
Exercise file
"""
from typing import Callable, Optional, Union
import redis
import uuid
import sys


class Cache:
    """ Redis cache class """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Constructor """
        random_id = str(uuid.uuid4())
        self._redis.set(random_id, data)
        return random_id

    def get(self, key: str,
            fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        """ Get originaltype data """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, value):
        """ Converts bytes to string """
        return value.decode("utf-8")

    def get_int(self, value):
        """ Converts bytes to integer """
        return int.from_bytes(value, sys.byteorder)
