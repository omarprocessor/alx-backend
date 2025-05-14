#!/usr/bin/env python3
"""LIFOCache module that implements a LIFO caching system."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a caching system that discards the last
    item added (LIFO) when the cache exceeds its maximum size."""

    def __init__(self):
        """Initialize the LIFO cache system."""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item in the cache using LIFO eviction policy.

        Args:
            key: The key under which to store the item.
            item: The item to be stored in the cache.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    last_key = self.stack.pop()
                    del self.cache_data[last_key]
                    print("DISCARD:", last_key)
                self.stack.append(key)
            else:
                self.stack.remove(key)
                self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
