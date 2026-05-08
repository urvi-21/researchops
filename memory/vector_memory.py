import os
import pickle
import faiss
import numpy as np


class VectorMemory:

    def __init__(
        self,
        dimension,
        memory_path="storage/vector_db/memory.index",
        metadata_path="storage/vector_db/memory.pkl"
    ):

        self.dimension = dimension

        self.memory_path = memory_path
        self.metadata_path = metadata_path

        self.index = faiss.IndexFlatL2(dimension)

        self.memory_entries = []

    def add_memory(
        self,
        embedding,
        content,
        metadata
    ):

        embedding = np.array([embedding]).astype("float32")

        self.index.add(embedding)

        self.memory_entries.append({
            "content": content,
            "metadata": metadata
        })

    def search_memory(
        self,
        query_embedding,
        top_k=5
    ):

        query_embedding = np.array(
            [query_embedding]
        ).astype("float32")

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx, score in zip(indices[0], distances[0]):

            if idx < len(self.memory_entries):

                results.append({
                    "score": float(score),
                    "memory": self.memory_entries[idx]
                })

        return results

    def save(self):

        os.makedirs(
            "storage/vector_db",
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            self.memory_path
        )

        with open(
            self.metadata_path,
            "wb"
        ) as f:

            pickle.dump(
                self.memory_entries,
                f
            )

        print("[SAVED] Vector Memory")

    def load(self):

        self.index = faiss.read_index(
            self.memory_path
        )

        with open(
            self.metadata_path,
            "rb"
        ) as f:

            self.memory_entries = pickle.load(f)

        print("[LOADED] Vector Memory")