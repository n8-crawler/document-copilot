from uuid import UUID
from sqlalchemy.orm import Session
from app.services.messageservice import MessageService
from app.services.threadservice import ThreadService
from app.models.users import User
from app.schemas.messages import MessageCreate
from app.embeddings.generator import EmbeddingGenerator
from app.retrieval.retriever import Retriver
from app.llm.prompt import PromptBuilder
from app.llm.generator import Llmgenerator
from app.graph.state import ChatState
from app.graph.graph import chat_graph
# its a orchestror createusermsg,retrive,promptbuild,generator,
class Chatservice:
    def __init__(self,db:Session):
        self.db = db

    # def getthread (self,thread_id:UUID,current_user:User):
    #     return ThreadService(self.db).get_thread(thread_id=thread_id,current_user=current_user)
    
    # def create_user_message(self,thread_id:UUID,current_user:User,request:MessageCreate):
    #     return MessageService(self.db).createusermessage(thread_id=thread_id,current_user=current_user,request=request)
    
    # def generate_embeddings(self,request:MessageCreate):
    #     content = request.messages
    #     return EmbeddingGenerator().generate_embeddings(text=content)
    
    # def retrive_chunks(self,embeddings):
    #     return Retriver(self.db).retrive(embeddings)
    
    # def chat_history(self,thread_id:UUID,current_user:User):
    #     return MessageService(self.db).get_messages(thread_id=thread_id,current_user=current_user)
    
    # def create_prompt(self,user_question:str,chunk_list:list,history=None):
    #     return PromptBuilder().build_prompt(user_question=user_question,chunk_list=chunk_list,history=history)
    
    # def llm_response(self,propmt:str):
    #     ai_message = Llmgenerator().generate(prompt=propmt)
    #     return ai_message
    
    def chat(self,thread_id:UUID,current_user:User,request:MessageCreate):

        state = ChatState(thread_id = thread_id,
                        request=request,
                        db = self.db, # this is even not required since in data class we are calling Session object but any way
                        current_user=current_user)
        result = chat_graph.invoke(state)

        # this will call builder.compile() which will call state as per sequence , since all dataclass ChatState values are populated

        return result.assistant_message

        # thread = self.getthread(thread_id=thread_id,current_user=current_user)
        # user_message = self.create_user_message(thread_id=thread_id,current_user=current_user,request=request)
        # embeddings = self.generate_embeddings(request=request)
        # chunks = self.retrive_chunks(embeddings=embeddings)
        # history = self.chat_history(thread_id=thread_id,current_user=current_user)
        # prompt = self.create_prompt(user_question=user_message.messages,chunk_list=chunks,history=history)
        # ai_response = self.llm_response(propmt=prompt)

        #save ai_message to create ai message and return orm obj which i will handle in router 
        # return MessageService(self.db).createassistantmessage(thread_id=thread_id,content=ai_response)
