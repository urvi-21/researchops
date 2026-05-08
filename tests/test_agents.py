from agents.retrieval_agent import RetrievalAgent
from agents.synthesis_agent import SynthesisAgent
from agents.insight_agent import InsightAgent
from agents.literature_review_agent import LiteratureReviewAgent
from agents.planning_agent import PlanningAgent
from agents.citation_agent import CitationAgent
from agents.memory_agent import MemoryAgent


query = "Applications of transformers in healthcare"

# =========================
# RETRIEVAL
# =========================

retrieval_agent = RetrievalAgent()

retrieval_output = retrieval_agent.run(query)

print("\n=== RETRIEVAL COMPLETE ===")

# =========================
# SYNTHESIS
# =========================

synthesis_agent = SynthesisAgent()

synthesis_output = synthesis_agent.run(
    query=query,
    retrieval_results=retrieval_output[
        "retrieved_contexts"
    ]
)

print("\n=== SYNTHESIS COMPLETE ===")

# =========================
# INSIGHTS
# =========================

insight_agent = InsightAgent()

insight_output = insight_agent.run(
    synthesis_output["synthesis"]
)

print("\n=== INSIGHTS COMPLETE ===")

# =========================
# LITERATURE REVIEW
# =========================

literature_agent = LiteratureReviewAgent()

literature_output = literature_agent.run(
    query=query,
    synthesis=synthesis_output[
        "synthesis"
    ]
)

print("\n=== LITERATURE REVIEW COMPLETE ===")

# =========================
# PLANNING
# =========================

planning_agent = PlanningAgent()

planning_output = planning_agent.run(
    insight_output["insights"]
)

print("\n=== PLANNING COMPLETE ===")

# =========================
# CITATIONS
# =========================

citation_agent = CitationAgent()

citation_output = citation_agent.run(
    retrieval_output["retrieved_contexts"]
)

print("\n=== CITATIONS COMPLETE ===")

# =========================
# MEMORY UPDATE
# =========================

memory_agent = MemoryAgent()

memory_agent.run(
    content=synthesis_output["synthesis"],
    metadata={
        "query": query,
        "type": "research_synthesis"
    }
)

print("\n=== MEMORY UPDATED ===")

# =========================
# FINAL OUTPUT
# =========================

print("\n==============================")
print("RESEARCHOPS AI AGENT TEST DONE")
print("==============================\n")

print("\n--- SYNTHESIS ---\n")
print(synthesis_output["synthesis"])

print("\n--- INSIGHTS ---\n")
print(insight_output["insights"])

print("\n--- ROADMAP ---\n")
print(planning_output["roadmap"])

print("\n--- CITATIONS ---\n")
print(citation_output["citations"])