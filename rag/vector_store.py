import os
import pickle
import faiss
import numpy as np


class FAISSVectorStore:

    def __init__(self, dimension):

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(dimension)

        self.documents = []

    def add_embeddings(self, embeddings, chunks):

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)

        self.documents.extend(chunks)

    def search(self, query_embedding, top_k=5):

        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx, score in zip(indices[0], distances[0]):

            if idx < len(self.documents):

                results.append({
                    "score": float(score),
                    "document": self.documents[idx]
                })

        return results

    def save(
        self,
        index_path="storage/vector_db/faiss.index",
        docs_path="storage/vector_db/documents.pkl"
    ):

        os.makedirs("storage/vector_db", exist_ok=True)

        faiss.write_index(self.index, index_path)

        with open(docs_path, "wb") as f:
            pickle.dump(self.documents, f)

        print("[SAVED] Vector DB")

    def load(
        self,
        index_path="storage/vector_db/faiss.index",
        docs_path="storage/vector_db/documents.pkl"
    ):

        self.index = faiss.read_index(index_path)

        with open(docs_path, "rb") as f:
            self.documents = pickle.load(f)

        print("[LOADED] Vector DB")