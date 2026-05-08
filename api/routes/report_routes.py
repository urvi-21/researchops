import os

from fastapi import APIRouter

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


REPORT_DIR = (
    "storage/reports"
)


@router.get("/")
def list_reports():

    reports = os.listdir(
        REPORT_DIR
    )

    return {
        "reports": reports
    }