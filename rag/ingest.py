from pathlib import Path
from pypdf import PdfReader


class DocumentIngestor:

    def __init__(self, docs_path: str):
        self.docs_path = Path(docs_path)

    def load_pdfs(self):
        """
        Load all PDFs from directory.
        """

        documents = []

        pdf_files = list(self.docs_path.glob("*.pdf"))

        for pdf_path in pdf_files:

            try:
                reader = PdfReader(str(pdf_path))

                full_text = ""

                for page in reader.pages:
                    text = page.extract_text()

                    if text:
                        full_text += text + "\n"

                documents.append({
                    "filename": pdf_path.name,
                    "filepath": str(pdf_path),
                    "text": full_text,
                    "pages": len(reader.pages)
                })

                print(f"[INGESTED] {pdf_path.name}")

            except Exception as e:
                print(f"[ERROR] {pdf_path.name}: {e}")

        return documents