# PrimeHomes Realty — Real Estate Lead Bot

AI-powered digital receptionist and lead management system for PrimeHomes Realty.

## Overview

This system automatically:

1. Receives customer enquiries (chat)
2. Understands natural language with AI (via n8n)
3. Extracts structured property requirements
4. Qualifies and scores leads
5. Stores everything in **MySQL** (local development)
6. Notifies the sales team for HOT leads
7. Provides a sales dashboard for follow-up

**Core principle:** AI handles repetitive qualification. Sales representatives handle relationship building and closing.

## Tech Stack (Local Development)

| Layer              | Technology              |
|--------------------|-------------------------|
| Frontend           | React + Vite (npm)      |
| Backend API        | FastAPI (Python)        |
| Database           | **MySQL** (local)       |
| Workflow / Automation | n8n                  |
| AI                 | LLM via n8n             |

> Docker is **not required** for local development. We use your existing MySQL installation.

## Project Structure

```text
Real-Estate-Bot-Nn/
│
├── frontend/          # React customer chat (orange/yellow UI)
├── backend/           # FastAPI application
├── n8n/               # Workflow definitions
├── database/          # Notes + future migrations
├── tests/
├── docs/              # All specifications
│
├── .env.example
├── .gitignore
└── README.md
```

## Quick Start (Local Development – No Docker)

### 1. MySQL

Create the database:

```sql
CREATE DATABASE real_estate_leads CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 2. Environment

```bash
cp .env.example .env
# Edit .env and set your MySQL password + n8n webhook URL
```

Example `DATABASE_URL`:
```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/real_estate_leads
```

### 3. Backend

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt

# Create tables
python create_tables.py

# Start API
uvicorn app.main:app --reload --port 8000
```

API docs: http://localhost:8000/docs

### 4. Frontend

```bash
cd frontend
npm install
npm run dev
```

Open: http://localhost:5173

### 5. n8n

Run n8n however you normally do (desktop app, npm, etc.).
Create a Webhook node that listens on the path you put in `N8N_WEBHOOK_URL`.

## Documentation

All product and technical specifications live in the `docs/` folder.

## License

MIT
