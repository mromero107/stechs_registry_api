from fastapi import FastAPI

from app.api.routes import router as v1_router
from app.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.include_router(v1_router, prefix="/api")
