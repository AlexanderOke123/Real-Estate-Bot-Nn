from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """Simple health check endpoint."""
    return {
        "status": "ok",
        "service": "primehomes-lead-bot",
        "version": "0.1.0",
    }
