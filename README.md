# PrimeHomes Realty — Real Estate Lead Bot

AI-powered digital receptionist and lead management system for PrimeHomes Realty.

## Overview

This system automatically:

1. Receives customer enquiries (chat)
2. Understands natural language with AI
3. Extracts structured property requirements
4. Qualifies and scores leads using deterministic rules
5. Stores everything in PostgreSQL (system of record)
6. Notifies the sales team for HOT leads
7. Provides a sales dashboard for follow-up and lifecycle management

**Core principle:** AI handles repetitive qualification and organization. Sales representatives handle relationship building and closing.

## Tech Stack

| Layer              | Technology              |
|--------------------|-------------------------|
| Frontend           | React                   |
| Backend API        | FastAPI (Python)        |
| Workflow / Automation | n8n                  |
| Database           | PostgreSQL              |
| AI                 | LLM (structured extraction) |
| Operational Reporting | Google Sheets        |
| Deployment         | Docker + single VPS     |

## Project Structure

```text
real-estate-lead-bot/
│
├── frontend/          # React customer chat + sales dashboard
├── backend/           # FastAPI application
├── n8n/               # Workflow definitions
├── database/          # Migrations, seeds, schema notes
├── tests/             # Shared / integration tests
├── docs/              # All specifications & design docs
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── docker-compose.prod.yml
└── README.md
```

## Quick Start (Local Development)

```bash
# 1. Clone
git clone https://github.com/AlexanderOke123/Real-Estate-Bot-Nn.git
cd Real-Estate-Bot-Nn

# 2. Environment
cp .env.example .env
# Edit .env with your values

# 3. Start infrastructure
docker compose up -d postgres n8n

# 4. Backend
cd backend
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
# Run migrations (once Alembic is set up)
uvicorn app.main:app --reload --port 8000

# 5. Frontend
cd ../frontend
npm install
npm run dev
```

Services will be available at:

- Frontend: http://localhost:3000 (or Vite default)
- Backend API: http://localhost:8000
- API docs: http://localhost:8000/docs
- n8n: http://localhost:5678
- PostgreSQL: localhost:5432

## Documentation

All product and technical specifications live in the `docs/` folder:

- **PRD** — Product Requirements Document
- **System Architecture Document (SAD)**
- **Database & Data Model Specification**
- **API Specification**
- **n8n Workflow Specification**
- **AI Specification**
- **UI-UX Specification**
- **Lead Qualification Spec**
- **Testing Spec**
- **Deployment Spec**
- **DEVELOPMENT_SETUP.md**
- **IMPLEMENTATION.md** (progress tracker)
- **TASK.md** (task board)

Start with `docs/PrimeHomes_Real_Estate_Lead_Bot_PRD_v1.0.md` and `docs/System Architecture Document (SAD).md`.

## Development Philosophy

1. **Simple first** — no premature microservices, Kubernetes, or message brokers.
2. **Clear responsibilities** — React = UI, FastAPI = business + API, n8n = orchestration, PostgreSQL = source of truth, AI = understanding only.
3. **Deterministic where it matters** — lead scoring and state transitions are rule-based, not pure AI.
4. **Human-in-the-loop** — AI never makes binding commitments or owns critical business decisions.
5. **Incremental** — build, test, document, then move to the next small task.

See `docs/IMPLEMENTATION.md` and `docs/TASK.md` for the current status and next tasks.

## License

MIT
