from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class LeadBase(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    property_type: Optional[str] = None
    bedrooms: Optional[int] = None
    location: Optional[str] = None
    budget_min: Optional[float] = None
    budget_max: Optional[float] = None
    currency: Optional[str] = "NGN"
    transaction_type: Optional[str] = None
    timeline: Optional[str] = None
    status: Optional[str] = None
    score: Optional[int] = None
    classification: Optional[str] = None


class LeadCreate(LeadBase):
    pass


class LeadUpdate(LeadBase):
    notes: Optional[str] = None
    assigned_to: Optional[str] = None


class LeadOut(LeadBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
