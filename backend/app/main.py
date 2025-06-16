from fastapi import FastAPI

from .db import engine
from .models import base

# Create all tables (for development/testing, not for production with Alembic)
base.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Personal App API"}
