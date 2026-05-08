from rag.retriever import Retriever


class RetrievalAgent:

    def __init__(self):

        self.retriever = Retriever()

        self.retriever.load_vector_store()

    def run(
        self,
        query,
        top_k=5
    ):

        results = self.retriever.retrieve(
            query=query,
            top_k=top_k
        )

        return {
            "query": query,
            "retrieved_contexts": results
        }