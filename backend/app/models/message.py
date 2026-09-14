import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import enum
from sqlalchemy import Enum as SAEnum

from app.db.session import Base


class MessageRole(str, enum.Enum):
    CUSTOMER = "customer"
    BOT = "bot"
    AGENT = "agent"
    SYSTEM = "system"


class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey("conversations.id"), nullable=False)
    lead_id = Column(UUID(as_uuid=True), ForeignKey("leads.id"), nullable=True)

    role = Column(SAEnum(MessageRole), nullable=False)
    content = Column(Text, nullable=False)

    # Idempotency / processing
    client_message_id = Column(String(255), nullable=True, index=True)
    processed = Column(Boolean, default=False)
    processing_error = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    conversation = relationship("Conversation", back_populates="messages")
    lead = relationship("Lead", back_populates="messages")

    def __repr__(self):
        return f"<Message {self.id} {self.role}>"
