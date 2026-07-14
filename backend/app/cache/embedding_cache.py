import json
from app.cache.redis import redis_client
class EmbeddingCache:
    PREFIX = "embedding:"

    def get(self,text:str):
        key = self.PREFIX + text
        result = redis_client.get(key)
        if result is None:return None
        json.loads(result)

    def set(self,text: str,embedding: list[float],ttl: int = 3600*24*7):
        key = self.PREFIX + text
        redis_client.set(key,json.dumps(embedding),ex=ttl)


