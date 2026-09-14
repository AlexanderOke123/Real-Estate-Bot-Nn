import uuid
from datetime import datetime
from sqlalchemy import (
    Column, String, Text, Integer, Float, DateTime, Enum as SAEnum
)
from sqlalchemy.orm import relationship
import enum

from app.db.session import Base


class TransactionType(str, enum.Enum):
    BUY = "BUY"
    RENT = "RENT"
    SELL = "SELL"
    INQUIRE = "INQUIRE"


class LeadStatus(str, enum.Enum):
    NEW = "NEW"
    QUALIFYING = "QUALIFYING"
    QUALIFIED = "QUALIFIED"
    ASSIGNED = "ASSIGNED"
    CONTACTED = "CONTACTED"
    ENGAGED = "ENGAGED"
    VIEWING_SCHEDULED = "VIEWING_SCHEDULED"
    NEGOTIATING = "NEGOTIATING"
    CONVERTED = "CONVERTED"
    LOST = "LOST"
    NURTURE = "NURTURE"


class LeadClassification(str, enum.Enum):
    HOT = "HOT"
    WARM = "WARM"
    COLD = "COLD"
    UNQUALIFIED = "UNQUALIFIED"


class Lead(Base):
    __tablename__ = "leads"

    # Use String(36) for UUID so it works cleanly with MySQL
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    preferred_contact_channel = Column(String(50), nullable=True)

    property_type = Column(String(100), nullable=True)
    bedrooms = Column(Integer, nullable=True)
    bathrooms = Column(Integer, nullable=True)
    location = Column(String(255), nullable=True)
    preferred_locations = Column(Text, nullable=True)
    budget_min = Column(Float, nullable=True)
    budget_max = Column(Float, nullable=True)
    currency = Column(String(10), default="NGN")
    property_condition = Column(String(100), nullable=True)

    transaction_type = Column(SAEnum(TransactionType), nullable=True)
    timeline = Column(String(50), nullable=True)

    status = Column(SAEnum(LeadStatus), default=LeadStatus.NEW, nullable=False)
    score = Column(Integer, nullable=True)
    classification = Column(SAEnum(LeadClassification), nullable=True)

    assigned_to = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_contact_at = Column(DateTime, nullable=True)

    conversations = relationship("Conversation", back_populates="lead", cascade="all, delete-orphan")
    messages = relationship("Message", back_populates="lead", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Lead {self.id} {self.status}>"
