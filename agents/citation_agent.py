class CitationAgent:

    def run(
        self,
        retrieval_results
    ):

        citations = []

        for result in retrieval_results:

            metadata = result["document"]["metadata"]

            citations.append({
                "source": metadata["source"],
                "chunk_id": metadata["chunk_id"]
            })

        return {
            "citations": citations
        }