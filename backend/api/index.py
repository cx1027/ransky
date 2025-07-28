import sys
import os
from pathlib import Path

# Add the backend directory to Python path
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

try:
    from app.main import app
except ImportError:
    # Fallback: create a minimal FastAPI app if imports fail
    from fastapi import FastAPI
    from starlette.middleware.cors import CORSMiddleware
    
    app = FastAPI(title="Ransky API")
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Try to import and include the router
    try:
        from app.api.main import api_router
        from app.core.config import settings
        app.include_router(api_router, prefix=settings.API_V1_STR)
    except ImportError:
        # If imports fail, add basic endpoints
        @app.get("/")
        async def root():
            return {"message": "Ransky API is running"}
        
        @app.get("/health")
        async def health():
            return {"status": "healthy"}

# This file serves as the entry point for Vercel serverless functions