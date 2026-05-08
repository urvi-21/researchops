import os

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from rag.ingestion_service import (
    IngestionService
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = (
    "storage/uploaded_docs"
)

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

ingestion_service = IngestionService()


@router.post("/pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:

        content = await file.read()

        f.write(content)

    ingestion_result = (
        ingestion_service.ingest_document(
            file_path
        )
    )

    return {
        "filename": file.filename,
        "status": "uploaded",
        "ingestion": ingestion_result
    }