from dataclasses import dataclass, field
from uuid import UUID
from sqlalchemy.orm import Session

from app.schemas.messages import MessageCreate
from app.models.users import User
from app.models.chatthreads import ChatThread
from app.models.chatmessage import ChatMessage

@dataclass
class ChatState:
#this we get from start when running the router
    thread_id:UUID
    request:MessageCreate
    db:Session
    current_user:User

# will populate this value as we go on calling thread(),usermessage,embedding etc..
    thread : ChatThread | None = None
    user_message:ChatMessage | None = None
    query_embedding: list[float] | None = None
    # retrieved_chunks: list = [] is not used becoz , it create shared list for every chat instance but factory list provide list for every chat instance
    retrived_chunk : list=field(default_factory=list) 
    history : list[ChatMessage]=field(default_factory=list)
    prompt :str=""
    ai_response: str=""
    assistant_message:ChatMessage | None=None