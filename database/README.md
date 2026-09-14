# Database

**Local development uses MySQL** (the instance already running on your machine).

PostgreSQL / Docker is reserved for later production deployment if needed.

## Core Entities

- `leads`
- `conversations`
- `messages`
- (future) users, roles, lead_scores, follow_ups, activities, etc.

## Local Setup (MySQL)

1. Make sure MySQL is running on your PC.
2. Create the database:

```sql
CREATE DATABASE real_estate_leads CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

3. Update `DATABASE_URL` in `.env` (or `backend/.env`):

```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/real_estate_leads
```

4. From the `backend/` folder run:

```bash
python create_tables.py
```

That creates the tables. You can also use Alembic later for proper migrations.

## Notes

- UUIDs are stored as `CHAR(36)` / `String(36)` for maximum MySQL compatibility.
- Google Sheets remains a secondary operational tool only.
