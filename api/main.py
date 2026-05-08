from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.workflow_routes import (
    router as workflow_router
)

from api.routes.upload_routes import (
    router as upload_router
)

from api.routes.report_routes import (
    router as report_router
)


# =========================
# FASTAPI APP
# =========================

app = FastAPI(
    title="ResearchOps AI",
    version="1.0.0"
)


# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# ROUTERS
# =========================

app.include_router(
    workflow_router
)

app.include_router(
    upload_router
)

app.include_router(
    report_router
)


# =========================
# ROOT ENDPOINT
# =========================

@app.get("/")

def root():

    return {
        "message":
            "ResearchOps AI Backend Running"
    }