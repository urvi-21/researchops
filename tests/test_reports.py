from workflows.research_workflow import (
    run_research_workflow
)


query = """
Transformer architectures
for medical imaging analysis
"""

result = run_research_workflow(
    query
)

print("\n========================")
print("REPORT GENERATED")
print("========================\n")

print(
    result["final_report"]
)