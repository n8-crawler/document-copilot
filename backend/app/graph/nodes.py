from app.graph.state import ChatState
from app.services.messageservice import MessageService
from app.services.threadservice import ThreadService
from app.embeddings.generator import EmbeddingGenerator
from app.llm.generator import Llmgenerator
from app.llm.prompt import PromptBuilder
from app.retrieval.retriever import Retriver


def getthread (state:ChatState) -> ChatState:
    state.thread= ThreadService(state.db).get_thread(thread_id=state.thread_id,current_user=state.current_user)
    return state

def create_user_message(state:ChatState):
    state.user_message =  MessageService(state.db).createusermessage(thread_id=state.thread_id,current_user=state.current_user,request=state.request)
    return state

def generate_embeddings(state:ChatState):
    content = state.request.messages
    state.query_embedding = EmbeddingGenerator().generate_embeddings(text=content)
    return state

def retrive_chunks(state:ChatState):
    state.retrived_chunk = Retriver(state.db).retrive(query=state.user_message.messages,query_embedding=state.query_embedding)
    return state

def chat_history(state:ChatState):
    state.history = MessageService(state.db).get_messages(thread_id=state.thread_id,current_user=state.current_user)
    return state

def create_prompt(state:ChatState):
    state.prompt = PromptBuilder().build_prompt(user_question=state.user_message.messages,chunk_list=state.retrived_chunk,history=state.history)
    return state

def llm_response(state:ChatState):
    state.ai_response = Llmgenerator().generate(prompt=state.prompt)
    return state

def save_ai_message(state:ChatState):
    state.assistant_message = MessageService(state.db).createassistantmessage(thread_id=state.thread_id,content=state.ai_response)
    return state