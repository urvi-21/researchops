from fastapi import APIRouter

from workflows.research_workflow import (
    run_research_workflow
)

router = APIRouter(
    prefix="/workflow",
    tags=["Workflow"]
)


@router.post("/run")
def run_workflow(
    query: str
):

    result = run_research_workflow(
        query
    )

    return {
        "status": "success",
        "report": result["final_report"]
    }