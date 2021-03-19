#!/usr/bin/python3
""" Brosqhdkjsqhdnksjq """


BaseCaching = __import__('BaseCaching').BaseCaching


class BasicCache(BaseCaching):
    """ 0-Brosqhdkjsqhdnksjq """

    def put(self, key, item):
        """ 0-Brosqhdkjsqhdnksjq """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ 0-Brosqhdkjsqhdnksjq """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
