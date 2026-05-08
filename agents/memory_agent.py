from rag.embeddings import EmbeddingModel
from memory.vector_memory import VectorMemory


class MemoryAgent:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        test_embedding = self.embedding_model.encode(
            ["memory"]
        )[0]

        dimension = len(test_embedding)

        self.vector_memory = VectorMemory(
            dimension
        )

    def run(
        self,
        content,
        metadata
    ):

        embedding = self.embedding_model.encode(
            [content]
        )[0]

        self.vector_memory.add_memory(
            embedding=embedding,
            content=content,
            metadata=metadata
        )

        self.vector_memory.save()

        return {
            "status": "memory_updated"
        }