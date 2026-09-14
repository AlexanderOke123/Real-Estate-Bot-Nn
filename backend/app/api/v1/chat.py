"""
Customer chat endpoint.

Flow:
1. React sends message → FastAPI
2. FastAPI stores customer message + creates/gets conversation & lead
3. FastAPI triggers n8n webhook (background)
4. FastAPI returns immediate acknowledgement
"""

import httpx
import uuid
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from typing import Optional, List

from app.db.session import get_db
from app.core.config import settings
from app.models import Lead, Conversation, Message, MessageRole, LeadStatus
from app.schemas.chat import ChatMessageCreate, ChatResponse, ChatMessageResponse

router = APIRouter()


async def trigger_n8n_workflow(
    conversation_id: str,
    lead_id: Optional[str],
    message_id: str,
    content: str,
    session_id: Optional[str],
):
    """Fire-and-forget call to n8n webhook."""
    payload = {
        "event": "customer_message",
        "conversation_id": conversation_id,
        "lead_id": lead_id,
        "message_id": message_id,
        "content": content,
        "session_id": session_id,
        "secret": settings.N8N_WEBHOOK_SECRET,
    }
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(settings.N8N_WEBHOOK_URL, json=payload)
            if resp.status_code >= 400:
                print(f"[n8n] webhook returned {resp.status_code}: {resp.text}")
    except Exception as e:
        # Never fail the customer request if n8n is down
        print(f"[n8n] webhook error: {e}")


@router.post("/chat", response_model=ChatResponse)
async def send_chat_message(
    body: ChatMessageCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    # 1. Get or create conversation
    conversation = None
    if body.conversation_id:
        conversation = db.query(Conversation).filter(Conversation.id == body.conversation_id).first()

    if not conversation:
        lead = Lead(status=LeadStatus.NEW)
        db.add(lead)
        db.flush()

        conversation = Conversation(
            lead_id=lead.id,
            session_id=body.session_id or str(uuid.uuid4()),
            channel="web_chat",
        )
        db.add(conversation)
        db.flush()
    else:
        lead = conversation.lead

    # 2. Idempotency
    if body.client_message_id:
        existing = (
            db.query(Message)
            .filter(Message.client_message_id == body.client_message_id)
            .first()
        )
        if existing:
            return ChatResponse(
                conversation_id=conversation.id,
                message=ChatMessageResponse(
                    id=existing.id,
                    role=existing.role.value,
                    content=existing.content,
                    created_at=existing.created_at,
                    conversation_id=conversation.id,
                ),
                bot_reply=None,
                status="accepted",
                lead_id=lead.id if lead else None,
            )

    # 3. Store customer message
    message = Message(
        conversation_id=conversation.id,
        lead_id=lead.id if lead else None,
        role=MessageRole.CUSTOMER,
        content=body.content.strip(),
        client_message_id=body.client_message_id,
        processed=False,
    )
    db.add(message)
    db.commit()
    db.refresh(message)

    # 4. Trigger n8n in background
    background_tasks.add_task(
        trigger_n8n_workflow,
        conversation_id=str(conversation.id),
        lead_id=str(lead.id) if lead else None,
        message_id=str(message.id),
        content=message.content,
        session_id=conversation.session_id,
    )

    return ChatResponse(
        conversation_id=conversation.id,
        message=ChatMessageResponse(
            id=message.id,
            role=message.role.value,
            content=message.content,
            created_at=message.created_at,
            conversation_id=conversation.id,
        ),
        bot_reply=None,
        status="accepted",
        lead_id=lead.id if lead else None,
    )


@router.get("/conversations/{conversation_id}/messages", response_model=List[ChatMessageResponse])
def get_conversation_messages(
    conversation_id: str,
    db: Session = Depends(get_db),
):
    messages = (
        db.query(Message)
        .filter(Message.conversation_id == conversation_id)
        .order_by(Message.created_at.asc())
        .all()
    )
    return [
        ChatMessageResponse(
            id=m.id,
            role=m.role.value,
            content=m.content,
            created_at=m.created_at,
            conversation_id=m.conversation_id,
        )
        for m in messages
    ]
