"""
From Andrew Candela's lecture 08-04-2020
Implement a LRU cache in as efficient a way as possible.

He decided to use an ordered dictionary. It has O(1) methods.

https://docs.python.org/3/library/collections.html#collections.OrderedDict

https://stackoverflow.com/questions/54808556/what-is-a-time-complexity-of-move-to-end-operation-for-ordereddict-in-python-3
https://stackoverflow.com/questions/8176513/ordereddict-performance-compared-to-deque

"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int = 10):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        '''
        Return the value stored at given key, if key exists.
        Otherwise, return -1. (Note: modify to return None if that is desired instead.)
        Move the entry of that key to the end of the cache, indicating that it's the most recently used item.
        '''
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def set(self, key: int, value: int) -> None:
        '''
        Insert the given key/value entry into the cache if the key isn't already there,
        otherwise, update the entry with that key to have the given value &
        move that entry to the end of the cache to indicate that it's the most recently used item.

        If the cache is at capacity, eject the least recently used item, 
        which is located at the beginning of the cache.
        '''
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
