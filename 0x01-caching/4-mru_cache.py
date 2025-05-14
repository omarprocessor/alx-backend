#!/usr/bin/env python3
"""MRUCache module that implements a Most
Recently Used (MRU) caching system."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache defines a caching system that discards the most
    recently used item first when the cache exceeds its max size."""

    def __init__(self):
        """Initialize the MRU cache system."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using MRU eviction policy.

        Args:
            key: The key under which to store the item.
            item: The item to be stored in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
