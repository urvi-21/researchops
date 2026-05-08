class WorkflowEvaluator:

    def evaluate_retrieval(
        self,
        retrieval_results
    ):

        return len(
            retrieval_results
        )

    def evaluate_citations(
        self,
        citations
    ):

        return len(
            citations
        )

    def evaluate_report(
        self,
        report
    ):

        return len(report)