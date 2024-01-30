#!/usr/bin/python3
'''1. FIFO caching
'''
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''A class FIFOCache that inherits from BasicCaching
    and is a caching system
    '''
    def __init__(self):
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        '''assign to the dictionary self.cache_data the
        item value for the key key
        '''
        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        '''return the value in self.cache_data linked to key
        '''
        with self.__rlock:
            return self.cache_data.get(key, None)

    def _balance(self, keyIn):
        """Removes the oldest item from the cache at MAX size
        """
        keyOut = None
        with self.__rlock:
            if keyIn not in self.__keys:
                keysLength = len(self.__keys)
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = self.__keys.pop(0)
                    self.cache_data.pop(keyOut)
                self.__keys.insert(keysLength, keyIn)
        return keyOut
