import json
from app.cache.redis import redis_client
class LlmCache:
    PREFIX = "llm:"

    def get(self,prompt:str):
        key = self.PREFIX + prompt
        result = redis_client.get(key)
        if result is None:return None
        json.loads(result)

    def set(self,prompt: str,ai_message: str,ttl: int = 3600*24*7):
        key = self.PREFIX + prompt
        redis_client.set(key,json.dumps(ai_message),ex=ttl)
        

