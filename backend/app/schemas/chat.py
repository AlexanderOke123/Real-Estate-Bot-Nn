from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID
from datetime import datetime


class ChatMessageCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=4000)
    session_id: Optional[str] = None
    client_message_id: Optional[str] = None
    conversation_id: Optional[UUID] = None


class ChatMessageResponse(BaseModel):
    id: UUID
    role: str
    content: str
    created_at: datetime
    conversation_id: UUID

    class Config:
        from_attributes = True


class ChatResponse(BaseModel):
    """Immediate response returned to the frontend."""
    conversation_id: UUID
    message: ChatMessageResponse
    bot_reply: Optional[str] = None  # May be null while n8n is processing
    status: str = "accepted"  # accepted | processing | completed
    lead_id: Optional[UUID] = None
