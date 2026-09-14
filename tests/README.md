# Tests

Shared and integration tests live here.

Backend unit/API tests also live under `backend/tests/`.

## Strategy (from TESTING_SPEC)

- Backend: unit + API + validation + auth
- AI: extraction, intent, missing fields, handoff, failure cases
- n8n: success path, duplicates, AI failure, API failure, notification failure
- Frontend: chat, error/retry, dashboard
- End-to-end: complete customer journey, HOT lead, incomplete lead, human handoff

Tests should be written alongside features, not deferred to the end.
