#!/usr/bin/env python3
""" LFUCache module that implements a Least
Frequently Used caching system """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache defines a LFU caching system with LRU fallback"""

    def __init__(self):
        """Initialize the LFU cache"""
        super().__init__()
        self.freq = {}
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using LFU + LRU algorithm

        Args:
            key: The key under which to store the item.
            item: The item to be stored in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find minimum frequency
                min_freq = min(self.freq.values())
                # Collect all keys with that frequency
                candidates = [k for k in self.order if self.freq[k] == min_freq]
                # The LRU of those candidates is the first one in order
                lfu_key = candidates[0]
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                self.order.remove(lfu_key)
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            self.freq[key] = 1
            self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache by key

        Args:
            key: The key for the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
