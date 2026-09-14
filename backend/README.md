# Backend — FastAPI Application

Primary application API and business logic layer.

## Responsibilities

- REST API endpoints
- Request / response validation
- Authentication & authorization
- Business rules (lead scoring, state transitions, etc.)
- Database access (SQLAlchemy + Alembic)
- Triggering n8n workflows via webhooks
- Security boundaries

## Must NOT

- Contain large multi-step automation workflows (those belong in n8n)
- Call AI providers for the main production extraction path (n8n orchestrates AI)
- Become a second source of truth

## Recommended Structure

```text
backend/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── leads.py
│   │       ├── conversations.py
│   │       ├── messages.py
│   │       ├── followups.py
│   │       └── health.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── core/               # config, security, dependencies
│   └── db/                 # session, base
│
├── alembic/
├── tests/
├── requirements.txt
├── Dockerfile
└── README.md
```

## Getting Started

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs will be available at http://localhost:8000/docs
