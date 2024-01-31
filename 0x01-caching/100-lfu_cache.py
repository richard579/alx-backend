#!/usr/bin/python3
'''5. LFU Caching
'''
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''An implementation of LFU(Least Frequently Used)
    '''
    def __init__(self):
        super().__init__()
        self.__stats = {}
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
            value = self.cache_data.get(key, None)
            if key in self.__stats:
                self.__stats[key] += 1
        return value

    def _balance(self, keyIn):
        """Removes the oldest item from the cache at MAX size
        """
        keyOut = None
        with self.__rlock:
            if keyIn not in self.__stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = min(self.__stats, key=self.__stats.get)
                    self.cache_data.pop(keyOut)
                    self.__stats.pop(keyOut)
            self.__stats[keyIn] = self.__stats.get(keyIn, 0) + 1
        return keyOut
