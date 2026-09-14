# Frontend — React Application

Customer-facing chat interface and internal sales dashboard.

## Responsibilities

- Chat UI for potential customers
- Lead forms / progressive information collection
- Sales login and dashboard
- Lead list, filters, details, conversation history
- Status updates, assignment, follow-up notes

## Must NOT

- Contain core business rules or lead scoring logic
- Access the database directly
- Call AI providers directly for production workflows
- Hold secrets or credentials

All communication goes through the FastAPI backend.

## Recommended Structure

```text
frontend/
│
├── src/
│   ├── components/
│   │   ├── ui/
│   │   ├── chat/
│   │   ├── leads/
│   │   ├── dashboard/
│   │   └── followups/
│   ├── pages/
│   │   ├── customer/
│   │   ├── auth/
│   │   └── dashboard/
│   ├── services/          # API client
│   ├── hooks/
│   ├── types/
│   ├── utils/
│   └── app/
│
├── public/
├── package.json
├── vite.config.ts          # or create-react-app equivalent
└── README.md
```

## Getting Started

```bash
cd frontend
npm install
npm run dev
```

Set `VITE_API_URL` (or equivalent) to point at the FastAPI backend.
