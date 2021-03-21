#!/usr/bin/env python3
""" Brosqhdkjsqhdnksjq """


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ 0-Brosqhdkjsqhdnksjq """
    def __init__(self):
        """ 0-Brosqhdkjsqhdnksjq """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ 0-Brosqhdkjsqhdnksjq """
        if key is None or item is None:
            return
        if len(self.keys) >= self.MAX_ITEMS:
            if key not in self.keys:
                print("DISCARD: {}".format(self.keys[-1]))
                del self.cache_data[self.keys[-1]]
            del self.keys[-1]
        self.keys = [key] + self.keys
        self.cache_data[key] = item

    def get(self, key):
        """ 0-Brosqhdkjsqhdnksjq """
        if not key or key not in self.cache_data.keys():
            return None
        del self.keys[self.keys.index(key)]
        self.keys = [key] + self.keys
        return self.cache_data[key]
