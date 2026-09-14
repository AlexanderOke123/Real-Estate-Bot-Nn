# Database

PostgreSQL is the **system of record** for all core application data.

## Core Entities (from specification)

- users
- roles
- leads
- conversations
- messages
- lead_scores
- lead_assignments
- follow_ups
- activities
- integration_syncs

## Tools

- SQLAlchemy models (in `backend/app/models/`)
- Alembic for migrations (to be configured in backend)

## Notes

- Google Sheets is secondary and must never become authoritative.
- All state transitions and scoring must be auditable and deterministic where possible.

See `docs/Database & Data Model Specification.md` for the full design.
