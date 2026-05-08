from rag.ingest import DocumentIngestor
from rag.chunking import DocumentChunker
from rag.embeddings import EmbeddingModel
from rag.vector_store import FAISSVectorStore


def build_rag_pipeline():

    print("\n=== RESEARCHOPS AI INGESTION ===\n")

    # 1. INGEST
    ingestor = DocumentIngestor(
        "data/sample_papers"
    )

    documents = ingestor.load_pdfs()

    print(f"\nLoaded {len(documents)} documents")

    # 2. CHUNK
    chunker = DocumentChunker()

    chunks = chunker.chunk_documents(documents)

    print(f"Generated {len(chunks)} chunks")

    # 3. EMBEDDINGS
    embedding_model = EmbeddingModel()

    texts = [chunk["content"] for chunk in chunks]

    embeddings = embedding_model.encode(texts)

    print("Generated embeddings")

    # 4. VECTOR STORE
    dimension = len(embeddings[0])

    vector_store = FAISSVectorStore(dimension)

    vector_store.add_embeddings(
        embeddings,
        chunks
    )

    vector_store.save()

    print("\n=== PIPELINE COMPLETE ===\n")


if __name__ == "__main__":
    build_rag_pipeline()