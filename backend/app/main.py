from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.health import router as health_router

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health_router, prefix=settings.API_V1_PREFIX, tags=["health"])


@app.get("/")
def root():
    return {
        "message": "PrimeHomes Real Estate Lead Bot API",
        "docs": "/docs",
        "health": f"{settings.API_V1_PREFIX}/health",
    }
