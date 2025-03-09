from fastapi import FastAPI
from app.routers import rackets
from app.database import engine
from app.models import Base

# Initialize DB
Base.metadata.create_all(bind=engine)

# Create FastAPI App
app = FastAPI()

# Include API routes
app.include_router(rackets.router)