from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ChatMessageCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=4000)
    session_id: Optional[str] = None
    client_message_id: Optional[str] = None
    conversation_id: Optional[str] = None


class ChatMessageResponse(BaseModel):
    id: str
    role: str
    content: str
    created_at: datetime
    conversation_id: str

    class Config:
        from_attributes = True


class ChatResponse(BaseModel):
    """Immediate response returned to the frontend."""
    conversation_id: str
    message: ChatMessageResponse
    bot_reply: Optional[str] = None
    status: str = "accepted"
    lead_id: Optional[str] = None
