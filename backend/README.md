# Backend

This directory contains the FastAPI application and database configuration.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

### Database

The application uses PostgreSQL. Configure the `DATABASE_URL` environment variable with your connection string.

Run Alembic migrations:

```bash
alembic upgrade head
```
