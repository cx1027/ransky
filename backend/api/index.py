import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware
import logging
import sys
import os
from pathlib import Path

from app.api.main import api_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Method 1: Navigate to parent, then to sibling folder
current_file = Path(__file__)
parent_dir = current_file.parent.parent  # Go up to parent
sibling_dir = parent_dir / "app"  # Go to sibling folder "app"
sys.path.insert(0, str(parent_dir))  # Add parent to path

logger.info(f"Current file: {current_file}")
logger.info(f"Parent directory: {parent_dir}")
logger.info(f"Sibling directory: {sibling_dir}")
logger.info(f"Python path: {sys.path}")

try:
    # Now we can import from sibling folder
    from app.api.main import api_router
    from app.core.config import settings
    logger.info("Successfully imported from sibling folder")
except ImportError as e:
    logger.error(f"Failed to import from sibling folder: {e}")
    raise

def custom_generate_unique_id(route: APIRoute) -> str:
    if route.tags:
        return f"{route.tags[0]}-{route.name}"
    return route.name

if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=settings.all_cors_origins,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

logger.info("FastAPI app initialized successfully")
