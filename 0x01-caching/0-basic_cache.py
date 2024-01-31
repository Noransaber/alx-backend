#!/usr/bin/python3
""" 0. Basic dictionary """

BaseCaching  = __import__( 'BaseCaching' ).BaseCaching

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
      if key == None or item == None:
        return 
      else:
        self.cache_data[key] = item

    
    def get(self, key):
      """
       return the value in self.cache_data linked to key.
      """
      if key == None:
        return None
      else:
        return self.cache_data.get(key)
