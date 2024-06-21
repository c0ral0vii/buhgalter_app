import redis
import json

class RedisCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.Redis(host=host, port=port, db=db)
        self.clear_cache()

    def add(self, key, value):
        if len(key) >= 2:
            self.redis_client.set(key, json.dumps(value))
            return True

    def get(self, key):
        return json.loads(self.redis_client.get(key))

    def get_all(self):
        all_data = {}
        for key in self.redis_client.keys('*'):
            key_str = key.decode('utf-8')
            value = self.redis_client.get(key_str)
            all_data[key_str] = json.loads(value) if value else None
        return all_data

    def clear_cache(self):
        try:
            self.redis_client.flushdb()
            return True
        except Exception as e:
            return False