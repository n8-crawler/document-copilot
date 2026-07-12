from datetime import datetime
from uuid import UUID
from pydantic import BaseModel,ConfigDict


class ChatCreate(BaseModel):
    title:str
    
class ChatUpdate(BaseModel):
    title:str | None=None

class ChatResponse(BaseModel):
    id:UUID
    title:str
    created_at:datetime
    updated_at:datetime
    model_config = ConfigDict(from_attributes=True)