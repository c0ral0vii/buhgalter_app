import json

class RedisCache:
    def __init__(self):
        self.cache = {}

    def add(self, key, value):
        if len(key) >= 2:
            self.cache.update({key: value})
            return True

    def add_new(self, key, value):
        if len(key) >= 2:
            self.cache.update({key: {'new_values': value}})
            return True

    def get(self, key):
        self.get_all()
        return self.cache.get(key)

    def get_all(self):
        return self.cache

    def clear_cache(self):
        self.cache.clear()