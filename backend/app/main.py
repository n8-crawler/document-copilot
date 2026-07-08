from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import users
from app.routers import auth

app = FastAPI(
    title="Document Copilot API",
    version="1.0.0",
    description="Backend API for Document Copilot",
)
 
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app.include_router(router=users.router)
app.include_router(router =auth.router)

@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "database": "configured",
    }