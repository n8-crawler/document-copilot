from ollama import Client
from app.config import settings

class Llmgenerator:
    def __init__(self):
        self.client = Client(host=settings.OLLAMA_BASE_URL)
    def generate(self,prompt:str):
        response = self.client.chat(model=settings.LLM_MODEL,messages=[{"role":"user","content":prompt}])
        return response["message"]["content"]