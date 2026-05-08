from langchain.text_splitter import RecursiveCharacterTextSplitter


class DocumentChunker:

    def __init__(
        self,
        chunk_size=1000,
        chunk_overlap=200
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def chunk_documents(self, documents):

        chunks = []

        for doc in documents:

            split_chunks = self.splitter.split_text(doc["text"])

            for idx, chunk in enumerate(split_chunks):

                chunks.append({
                    "content": chunk,
                    "metadata": {
                        "source": doc["filename"],
                        "chunk_id": idx,
                        "pages": doc["pages"]
                    }
                })

        return chunks