from rag.embeddings import EmbeddingModel
from rag.vector_store import FAISSVectorStore


class Retriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.vector_store = None

    def load_vector_store(self):

        test_embedding = self.embedding_model.encode(
            ["test"]
        )[0]

        dimension = len(test_embedding)

        self.vector_store = FAISSVectorStore(dimension)

        self.vector_store.load()

    def retrieve(
        self,
        query,
        top_k=5
    ):

        query_embedding = self.embedding_model.encode(
            [query]
        )[0]

        results = self.vector_store.search(
            query_embedding,
            top_k
        )

        return results