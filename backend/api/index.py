import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware
import logging
import sys
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Log the current working directory and Python path
logger.info(f"Current working directory: {os.getcwd()}")
logger.info(f"Python path: {sys.path}")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

logger.info(f"Updated Python path: {sys.path}")

try:
    from backend.app.api.main import api_router
    from backend.app.core.config import settings
    logger.info("Successfully imported api_router and settings")
except ImportError as e:
    logger.error(f"Failed to import modules: {e}")
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
