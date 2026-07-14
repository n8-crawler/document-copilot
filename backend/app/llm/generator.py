from ollama import Client
from app.config import settings
from app.cache.llm_cache import LlmCache

class Llmgenerator:
    def __init__(self):
        self.client = Client(host=settings.OLLAMA_BASE_URL)

    def generate(self,prompt:str):
        ai_message = LlmCache().get(prompt)
        if ai_message:
            print("got from llm cache")
            return ai_message
        response = self.client.chat(model=settings.LLM_MODEL,messages=[{"role":"user","content":prompt}])
        LlmCache().set(prompt=prompt,ai_message=response["message"]["content"])

        return response["message"]["content"]