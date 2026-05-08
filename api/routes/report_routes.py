from fastapi import APIRouter
from fastapi.responses import FileResponse

import os


router = APIRouter()

REPORTS_DIR = "storage/reports"


# =========================
# LIST REPORTS
# =========================

@router.get("/reports")

def list_reports():

    reports = []

    if os.path.exists(REPORTS_DIR):

        for file in os.listdir(REPORTS_DIR):

            if file.endswith(".md"):

                reports.append(file)

    reports.sort(reverse=True)

    return {
        "reports": reports
    }


# =========================
# GET REPORT CONTENT
# =========================

@router.get("/reports/{report_name}")

def get_report(report_name: str):

    report_path = os.path.join(
        REPORTS_DIR,
        report_name
    )

    if not os.path.exists(report_path):

        return {
            "error": "Report not found"
        }

    with open(
        report_path,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    return {
        "report_name": report_name,
        "content": content
    }


# =========================
# DOWNLOAD REPORT
# =========================

@router.get("/reports/download/{report_name}")

def download_report(report_name: str):

    report_path = os.path.join(
        REPORTS_DIR,
        report_name
    )

    return FileResponse(
        report_path,
        media_type="text/markdown",
        filename=report_name
    )