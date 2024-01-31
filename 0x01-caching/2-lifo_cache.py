#!/usr/bin/env python3

'''Task 2. LIFO Caching
'''

from base_caching import BaseCaching


class LIFOCache (BaseCaching):
    """
    LIFOCache is a subclass of BaseCaching that implements
    the LRU cache algorithm."""

    def __init__(self):
        """
        LIFOCache is a subclass of BaseCaching that implements"""
        super().__init__()

    def put(self, key, item):
        """
        LIFOCache.put(key, item) -> None"""
        if key is not None or item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(True)
            print("DISCARD: " last_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

def get(self, key):
    """
    LIFOCache.get(key) -> item"""
    return self.cache_data.get(key)
