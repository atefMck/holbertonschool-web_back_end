#!/usr/bin/env python3
"""
Web file
"""
import requests
import redis
from functools import wraps

store = redis.Redis()
store.flushdb()

def count_url_access(method):
    """ Decorator counting how many times
    a Url is accessed """
    @wraps(method)
    def wrapper(url):
        count_key = "count:" + url
        html = method(url)
        store.incr(count_key)
        store.expire(count_key, 10)
        return html
    return wrapper

@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    return res.text
