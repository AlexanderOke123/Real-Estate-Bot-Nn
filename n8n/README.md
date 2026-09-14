# n8n Workflows

n8n is the workflow orchestration and integration layer.

## Responsibilities

- Receive events/webhooks from FastAPI
- Orchestrate AI processing
- Call validation and qualification steps
- Send notifications
- Synchronize selected data to Google Sheets
- Handle scheduled follow-up reminders
- Workflow-level retries and error handling

## Must NOT

- Become the primary application database
- Own core business rules that should live in FastAPI
- Be the only place critical data is stored

## Recommended Workflow Names

| Workflow ID                    | Purpose                              |
|--------------------------------|--------------------------------------|
| `PRH-LEAD-PROCESS-MESSAGE`     | Main customer message processing     |
| `PRH-LEAD-QUALIFY`             | Deterministic scoring & classification |
| `PRH-LEAD-NOTIFY-SALES`        | HOT lead notifications               |
| `PRH-FOLLOWUP-REMINDER`        | Due follow-up reminders              |
| `PRH-SHEET-SYNC-LEAD`          | Optional Google Sheets sync          |
| `PRH-ERROR-HANDLER`            | Centralised error capture            |

## Structure

```text
n8n/
│
├── workflows/
│   ├── lead-process-message.json   # (to be created)
│   ├── lead-qualify.json
│   ├── lead-notify-sales.json
│   ├── followup-reminder.json
│   ├── sheet-sync-lead.json
│   └── error-handler.json
│
└── README.md
```

Export workflows from the n8n UI and place the JSON files here for version control.
