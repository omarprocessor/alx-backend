#!/usr/bin/env python3
"""FIFOCache module that implements a FIFO caching system."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a caching system that discards the first
    item added (FIFO) when the cache exceeds its maximum size."""

    def __init__(self):
        """Initialize the FIFO cache system."""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item in the cache using FIFO eviction policy.

        Args:
            key: The key under which to store the item.
            item: The item to be stored in the cache.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded = self.queue.pop(0)
                    del self.cache_data[discarded]
                    print("DISCARD:", discarded)
                self.queue.append(key)
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
