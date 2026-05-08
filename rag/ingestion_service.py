import os

from pathlib import Path

from pypdf import PdfReader

from rag.chunking import DocumentChunker
from rag.embeddings import EmbeddingModel
from rag.vector_store import FAISSVectorStore

from memory.metadata_store import (
    MetadataStore
)


class IngestionService:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.chunker = DocumentChunker()

        self.metadata_store = MetadataStore()

    def ingest_document(
        self,
        file_path
    ):

        print(
            f"\n[INGESTION] Processing: {file_path}"
        )

        file_path = str(
            Path(file_path).resolve()
        )

        pdf_path = Path(file_path)

        # =====================
        # PDF READING
        # =====================

        reader = PdfReader(file_path)

        full_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:

                full_text += text + "\n"

        document = {
            "filename": pdf_path.name,
            "filepath": file_path,
            "text": full_text,
            "pages": len(reader.pages)
        }

        # =====================
        # CHUNKING
        # =====================

        chunks = self.chunker.chunk_documents(
            [document]
        )

        texts = [
            chunk["content"]
            for chunk in chunks
        ]

        # =====================
        # EMBEDDINGS
        # =====================

        embeddings = self.embedding_model.encode(
            texts
        )

        # =====================
        # VECTOR STORE
        # =====================

        dimension = len(embeddings[0])

        vector_store = FAISSVectorStore(
            dimension
        )

        index_exists = os.path.exists(
            "storage/vector_db/faiss.index"
        )

        if index_exists:

            vector_store.load()

        vector_store.add_embeddings(
            embeddings,
            chunks
        )

        vector_store.save()

        # =====================
        # METADATA
        # =====================

        self.metadata_store.add_document(
            filename=document["filename"],
            filepath=document["filepath"],
            topic="uploaded_research",
            pages=document["pages"]
        )

        print(
            "[INGESTION] Complete"
        )

        return {
            "filename":
                document["filename"],
            "chunks_added":
                len(chunks),
            "status":
                "ingested"
        }