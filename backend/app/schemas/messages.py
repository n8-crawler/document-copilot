from datetime import datetime
from uuid import UUID
from pydantic import BaseModel,ConfigDict

class MessageCreate(BaseModel):
    messages:str


class MessageResponse(BaseModel):
    id:UUID
    role:str
    messages:str
    prompt_tokens:int | None=None
    completion_tokens:int | None=None
    created_at:datetime

    model_config = ConfigDict(from_attributes=True)