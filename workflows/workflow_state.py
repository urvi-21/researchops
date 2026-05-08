from typing import TypedDict, List, Dict, Any


class ResearchWorkflowState(TypedDict):

    query: str

    retrieval_results: List[Dict[str, Any]]

    synthesis: str

    insights: str

    literature_review: str

    roadmap: str

    citations: List[Dict[str, Any]]

    final_report: str