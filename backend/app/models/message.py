import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Boolean, Enum as SAEnum
from sqlalchemy.orm import relationship
import enum

from app.db.session import Base


class MessageRole(str, enum.Enum):
    CUSTOMER = "customer"
    BOT = "bot"
    AGENT = "agent"
    SYSTEM = "system"


class Message(Base):
    __tablename__ = "messages"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    conversation_id = Column(String(36), ForeignKey("conversations.id"), nullable=False)
    lead_id = Column(String(36), ForeignKey("leads.id"), nullable=True)

    role = Column(SAEnum(MessageRole), nullable=False)
    content = Column(Text, nullable=False)

    client_message_id = Column(String(255), nullable=True, index=True)
    processed = Column(Boolean, default=False)
    processing_error = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    conversation = relationship("Conversation", back_populates="messages")
    lead = relationship("Lead", back_populates="messages")

    def __repr__(self):
        return f"<Message {self.id} {self.role}>"
