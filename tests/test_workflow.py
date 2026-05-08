from workflows.research_workflow import (
    run_research_workflow
)


query = """
Applications of transformers
in medical imaging
"""

result = run_research_workflow(
    query
)

print("\n========================")
print("RESEARCHOPS AI WORKFLOW")
print("========================\n")

print(
    result["final_report"]
)
