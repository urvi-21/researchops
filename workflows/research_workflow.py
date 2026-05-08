from langgraph.graph import StateGraph, END

from workflows.workflow_state import (
    ResearchWorkflowState
)

from reports.report_generator import (
    ReportGenerator
)

from tracking.mlflow_tracker import (
    MLflowTracker
)

from tracking.evaluation import (
    WorkflowEvaluator
)

from tracking.logger import logger

from agents.retrieval_agent import RetrievalAgent
from agents.synthesis_agent import SynthesisAgent
from agents.insight_agent import InsightAgent
from agents.literature_review_agent import (
    LiteratureReviewAgent
)
from agents.planning_agent import PlanningAgent
from agents.citation_agent import CitationAgent
from agents.memory_agent import MemoryAgent


# =========================
# AGENT INITIALIZATION
# =========================

retrieval_agent = RetrievalAgent()

synthesis_agent = SynthesisAgent()

insight_agent = InsightAgent()

literature_agent = LiteratureReviewAgent()

planning_agent = PlanningAgent()

citation_agent = CitationAgent()

memory_agent = MemoryAgent()

report_generator = ReportGenerator()

mlflow_tracker = MLflowTracker()

evaluator = WorkflowEvaluator()


# =========================
# RETRIEVAL NODE
# =========================

def retrieval_node(
    state: ResearchWorkflowState
):

    try:

        logger.info(
            "Starting Retrieval Node"
        )

        output = retrieval_agent.run(
            query=state["query"]
        )

        retrieval_count = evaluator.evaluate_retrieval(
            output["retrieved_contexts"]
        )

        mlflow_tracker.log_metric(
            "retrieved_chunks",
            retrieval_count
        )

        logger.info(
            "Retrieval Node Complete"
        )

        return {
            "retrieval_results":
                output["retrieved_contexts"]
        }

    except Exception as e:

        logger.error(
            f"Retrieval Node Failed: {e}"
        )

        return {
            "retrieval_results": []
        }


# =========================
# SYNTHESIS NODE
# =========================

def synthesis_node(
    state: ResearchWorkflowState
):

    try:

        logger.info(
            "Starting Synthesis Node"
        )

        output = synthesis_agent.run(
            query=state["query"],
            retrieval_results=state[
                "retrieval_results"
            ]
        )

        logger.info(
            "Synthesis Node Complete"
        )

        return {
            "synthesis":
                output["synthesis"]
        }

    except Exception as e:

        logger.error(
            f"Synthesis Node Failed: {e}"
        )

        return {
            "synthesis":
                "Synthesis generation failed."
        }


# =========================
# INSIGHT NODE
# =========================

def insight_node(
    state: ResearchWorkflowState
):

    try:

        logger.info(
            "Starting Insight Node"
        )

        output = insight_agent.run(
            state["synthesis"]
        )

        logger.info(
            "Insight Node Complete"
        )

        return {
            "insights":
                output["insights"]
        }

    except Exception as e:

        logger.error(
            f"Insight Node Failed: {e}"
        )

        return {
            "insights":
                "Insight generation failed."
        }


# =========================
# LITERATURE NODE
# =========================

def literature_node(
    state: ResearchWorkflowState
):

    try:

        logger.info(
            "Starting Literature Review Node"
        )

        output = literature_agent.run(
            query=state["query"],
            synthesis=state["synthesis"]
        )

        logger.info(
            "Literature Review Node Complete"
        )

        return {
            "literature_review":
                output["literature_review"]
        }

    except Exception as e:

        logger.error(
            f"Literature Node Failed: {e}"
        )

        return {
            "literature_review":
                "Literature review generation failed."
        }


# =========================
# PLANNING NODE
# =========================

def planning_node(
    state: ResearchWorkflowState
):

    try:

        logger.info(
            "Starting Planning Node"
        )

        output = planning_agent.run(
            state["insights"]
        )

        logger.info(
            "Planning Node Complete"
        )

        return {
            "roadmap":
                output["roadmap"]
        }

    except Exception as e:

        logger.error(
            f"Planning Node Failed: {e}"
        )

        return {
            "roadmap":
                "Roadmap generation failed."
        }


# =========================
# CITATION NODE
# =========================

def citation_node(
    state: ResearchWorkflowState
):

    try:

        logger.info(
            "Starting Citation Node"
        )

        output = citation_agent.run(
            state["retrieval_results"]
        )

        citation_count = evaluator.evaluate_citations(
            output["citations"]
        )

        mlflow_tracker.log_metric(
            "citation_count",
            citation_count
        )

        logger.info(
            "Citation Node Complete"
        )

        return {
            "citations":
                output["citations"]
        }

    except Exception as e:

        logger.error(
            f"Citation Node Failed: {e}"
        )

        return {
            "citations": []
        }


# =========================
# MEMORY NODE
# =========================

def memory_node(
    state: ResearchWorkflowState
):

    try:

        logger.info(
            "Starting Memory Node"
        )

        memory_agent.run(
            content=state["synthesis"],
            metadata={
                "query": state["query"],
                "type": "workflow_synthesis"
            }
        )

        logger.info(
            "Memory Node Complete"
        )

        return {}

    except Exception as e:

        logger.error(
            f"Memory Node Failed: {e}"
        )

        return {}


# =========================
# REPORT NODE
# =========================

def report_node(
    state: ResearchWorkflowState
):

    try:

        logger.info(
            "Generating Final Report"
        )

        report = report_generator.generate_report(
            state
        )

        report_length = evaluator.evaluate_report(
            report
        )

        mlflow_tracker.log_metric(
            "report_length",
            report_length
        )

        mlflow_tracker.log_text(
            report,
            "final_report.md"
        )

        saved_path = report_generator.save_report(
            report
        )

        logger.info(
            f"Report Saved: {saved_path}"
        )

        return {
            "final_report": report
        }

    except Exception as e:

        logger.error(
            f"Report Node Failed: {e}"
        )

        return {
            "final_report":
                "Report generation failed."
        }


# =========================
# LANGGRAPH
# =========================

workflow = StateGraph(
    ResearchWorkflowState
)

workflow.add_node(
    "retrieval",
    retrieval_node
)

workflow.add_node(
    "synthesis",
    synthesis_node
)

workflow.add_node(
    "insights",
    insight_node
)

workflow.add_node(
    "literature",
    literature_node
)

workflow.add_node(
    "planning",
    planning_node
)

workflow.add_node(
    "citations",
    citation_node
)

workflow.add_node(
    "memory",
    memory_node
)

workflow.add_node(
    "report",
    report_node
)


# =========================
# WORKFLOW EDGES
# =========================

workflow.set_entry_point(
    "retrieval"
)

workflow.add_edge(
    "retrieval",
    "synthesis"
)

workflow.add_edge(
    "synthesis",
    "insights"
)

workflow.add_edge(
    "insights",
    "literature"
)

workflow.add_edge(
    "literature",
    "planning"
)

workflow.add_edge(
    "planning",
    "citations"
)

workflow.add_edge(
    "citations",
    "memory"
)

workflow.add_edge(
    "memory",
    "report"
)

workflow.add_edge(
    "report",
    END
)


# =========================
# COMPILE GRAPH
# =========================

research_graph = workflow.compile()


# =========================
# EXECUTION FUNCTION
# =========================

def run_research_workflow(
    query: str
):

    logger.info(
        "Research Workflow Started"
    )

    mlflow_tracker.start_run(
        run_name="research_workflow"
    )

    mlflow_tracker.log_param(
        "query",
        query
    )

    result = research_graph.invoke({

        "query": query,

        "retrieval_results": [],

        "synthesis": "",

        "insights": "",

        "literature_review": "",

        "roadmap": "",

        "citations": [],

        "final_report": ""
    })

    mlflow_tracker.end_run()

    logger.info(
        "Research Workflow Complete"
    )

    return result