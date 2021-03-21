#!/usr/bin/env python3


BaseCaching = __import__('base_caching').BaseCaching


class CacheNode:
    """ 0-Brosqhdkjsqhdnksjq """

    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

    def append(self, cache):
        cache.prev = self
        self.next = cache


class FreqNode:
    """ 0-Brosqhdkjsqhdnksjq """

    def __init__(self, val):
        self.frequency = val
        self.cache = None
        self.next = None
        self.prev = None

    def append(self, FreqNode):
        FreqNode.prev = self
        if self.next:
            FreqNode.next = self.next
            self.next.prev = FreqNode
        self.next = FreqNode

    def preppend(self, FreqNode):
        FreqNode.next = self
        if self.prev:
            FreqNode.prev = self.prev
            self.prev.next = FreqNode
        self.prev = FreqNode

    def insertCache(self, cache):
        itr = self.cache
        if not itr:
            self.cache = cache
            return
        while itr:
            if itr.next is None:
                itr.append(cache)
                return
            itr = itr.next

    def removeCache(self, key):
        itr = self.cache
        while itr:
            if itr.key == key:
                if itr.next:
                    if itr.prev:
                        itr.next.prev = itr.prev
                        itr.prev.next = itr.next
                    else:
                        itr.next.prev = None
                        self.cache = itr.next
                else:
                    if itr.prev:
                        itr.prev.next = None
                if not itr.next and not itr.prev:
                    self.cache = None
                itr = None
                return
            itr = itr.next


class FreqList:
    def __init__(self):
        self.head = FreqNode(0)

    def insertCache(self, freq, cache):
        itr = self.head
        while itr:
            if itr.frequency == freq:
                itr.insertCache(cache)
                return
            elif itr.frequency > freq:
                newFreq = FreqNode(freq)
                newFreq.insertCache(cache)
                itr.preppend(newFreq)
                return
            elif itr.next is None:
                itr.next = FreqNode(freq)
                itr.next.insertCache(cache)
                return
            itr = itr.next

    def getFrequency(self, key):
        itr = self.head
        while itr:
            itrc = itr.cache
            while itrc:
                if itrc.key == key:
                    return itr.frequency
                itrc = itrc.next
            itr = itr.next
        return 0

    def getCacheNumAtFreq(self, freq):
        itr = self.head
        i = 0
        while itr:
            if itr.frequency == freq:
                itrc = itr.cache
                while itrc:
                    i = i + 1
                    itrc = itrc.next
                return i
            itr = itr.next
        return i

    def removeLRUCache(self, freq):
        itr = self.head
        while itr:
            if itr.frequency == freq:
                if itr.cache.next:
                    itr.cache.next.prev = None
                aux = itr.cache
                r = aux.key
                itr.cache = itr.cache.next
                aux = None
                return r
            itr = itr.next

    def updateCache(self, key, value):
        itr = self.head
        newFreq = self.getFrequency(key) + 1
        while itr:
            if itr.frequency == self.getFrequency(key):
                itr.removeCache(key)
            itr = itr.next
        self.insertCache(newFreq, CacheNode(key, value))

    def removeLFUCache(self):
        itr = self.head
        while itr:
            if self.getCacheNumAtFreq(itr.frequency) > 1:
                return self.removeLRUCache(itr.frequency)
            itr = itr.next

    def printFreq(self):
        itr = self.head
        while itr:
            print(itr.frequency, end="")
            itrc = itr.cache
            while itrc:
                print(" -> {} : {}".format(itrc.key, itrc.val), end="")
                itrc = itrc.next
            print()
            itr = itr.next


class LFUCache(BaseCaching):
    """ 0-Brosqhdkjsqhdnksjq """

    def __init__(self):
        """ 0-Brosqhdkjsqhdnksjq """
        super().__init__()
        self.freq_list = FreqList()

    def put(self, key, item):
        """ 0-Brosqhdkjsqhdnksjq """
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) == self.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.freq_list.updateCache(key, item)
                self.cache_data[key] = item
            else:
                # print("=====================================")
                # self.freq_list.printFreq()
                # print(self.cache_data)
                # print("=====================================")
                self.freq_list.insertCache(1, CacheNode(key, item))
                removed = self.freq_list.removeLFUCache()
                del self.cache_data[removed]
                self.cache_data[key] = item
                print("DISCARD: {}".format(removed))
        else:
            self.freq_list.insertCache(1, CacheNode(key, item))
            self.cache_data[key] = item

    def get(self, key):
        """ 0-Brosqhdkjsqhdnksjq """
        if not key or key not in self.cache_data.keys():
            return None
        self.freq_list.updateCache(key, self.cache_data[key])
        return self.cache_data[key]
