#!/usr/bin/env python3

'''Task 0: Basic dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Define the value in self.cache_data linked to key.
    """

    def __init__(self):
        """
        init function inhert from the base class
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
         return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
