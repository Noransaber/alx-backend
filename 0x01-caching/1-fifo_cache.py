#!/usr/bin/env python3

'''Task 1. FIFO caching
'''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a subclass of BaseCaching.
    """

    def __init__(self):
        """
        Initialize the FIFOCache class.
        """
        super().__init__()

    def put(self, key, item):
        """
        Put an item in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = list(self.cache_data)[0]
                self.cache_data.pop(discarded_key)
                print("DISCARD: " + str(discarded_key))

    def get(self, key):
        """
        return the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
