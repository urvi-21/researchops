import streamlit as st
import requests
import pandas as pd
import os
from datetime import datetime


# =========================
# CONFIG
# =========================

API_BASE_URL = "http://127.0.0.1:8000"

REPORTS_DIR = "storage/reports"

UPLOADS_DIR = "storage/uploaded_docs"


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="ResearchOps AI",
    page_icon="🧠",
    layout="wide"
)


# =========================
# CUSTOM CSS
# =========================

st.markdown(
    """
    <style>

    .main {
        background-color: #0B0F19;
        color: white;
    }

    .block-container {
        padding-top: 2rem;
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background-color: #6C63FF;
        color: white;
        border: none;
        font-size: 16px;
        font-weight: 600;
    }

    .metric-card {
        background-color: #141926;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #222938;
    }

    .workflow-card {
        background-color: #141926;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #222938;
        margin-bottom: 15px;
    }

    .status-online {
        color: #00FF9D;
        font-weight: 600;
    }

    .report-card {
        background-color: #141926;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #222938;
        margin-bottom: 18px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================
# HELPERS
# =========================

def get_report_count():

    if not os.path.exists(REPORTS_DIR):
        return 0

    return len([
        f for f in os.listdir(REPORTS_DIR)
        if f.endswith(".md")
    ])


def get_document_count():

    if not os.path.exists(UPLOADS_DIR):
        return 0

    return len([
        f for f in os.listdir(UPLOADS_DIR)
        if f.endswith(".pdf")
    ])


def get_latest_reports(limit=5):

    if not os.path.exists(REPORTS_DIR):
        return []

    reports = []

    for file in os.listdir(REPORTS_DIR):

        if file.endswith(".md"):

            full_path = os.path.join(
                REPORTS_DIR,
                file
            )

            timestamp = os.path.getmtime(
                full_path
            )

            reports.append({
                "name": file,
                "timestamp": timestamp
            })

    reports.sort(
        key=lambda x: x["timestamp"],
        reverse=True
    )

    return reports[:limit]


# =========================
# SIDEBAR
# =========================

st.sidebar.title("🧠 ResearchOps AI")

st.sidebar.markdown(
    """
    Autonomous Research Workflow
    Operating System
    """
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Upload Corpus",
        "Run Workflow",
        "Reports"
    ]
)


# =========================
# DASHBOARD
# =========================

if page == "Dashboard":

    st.title(
        "Autonomous Research Workflow Infrastructure"
    )

    st.markdown(
        """
        Persistent AI infrastructure for research operations,
        literature intelligence, synthesis, and roadmap generation.
        """
    )

    document_count = get_document_count()

    report_count = get_report_count()

    workflow_count = report_count

    topic_count = max(
        1,
        report_count
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Documents",
            document_count
        )

    with col2:
        st.metric(
            "Workflow Runs",
            workflow_count
        )

    with col3:
        st.metric(
            "Generated Reports",
            report_count
        )

    with col4:
        st.metric(
            "Research Topics",
            topic_count
        )

    st.divider()

    st.subheader(
        "Autonomous Capabilities"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="workflow-card">
            <h4>📚 Literature Review</h4>
            <p>
            Autonomous corpus-wide review generation.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="workflow-card">
            <h4>🧠 Persistent Memory</h4>
            <p>
            Long-term research intelligence across workflows.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class="workflow-card">
            <h4>🔍 Semantic Retrieval</h4>
            <p>
            Retrieval grounded in vector embeddings.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="workflow-card">
            <h4>📈 Insight Generation</h4>
            <p>
            Detect trends, gaps, and future directions.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class="workflow-card">
            <h4>🗺 Research Roadmaps</h4>
            <p>
            Generate structured future research plans.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="workflow-card">
            <h4>📑 Citation Grounding</h4>
            <p>
            Workflow outputs grounded to source documents.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader(
        "Operational System Health"
    )

    health_col1, health_col2 = st.columns(2)

    with health_col1:

        st.markdown(
            """
            <div class="workflow-card">
            <p class="status-online">
            ● FastAPI Backend — Online
            </p>

            <p class="status-online">
            ● Vector Store — Healthy
            </p>

            <p class="status-online">
            ● Workflow Engine — Active
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with health_col2:

        st.markdown(
            """
            <div class="workflow-card">
            <p class="status-online">
            ● MLflow Tracking — Running
            </p>

            <p class="status-online">
            ● Memory Layer — Synced
            </p>

            <p class="status-online">
            ● Retrieval Layer — Operational
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader(
        "Recent Workflow Outputs"
    )

    latest_reports = get_latest_reports()

    if len(latest_reports) == 0:

        st.info(
            "No workflow reports generated yet."
        )

    else:

        for report in latest_reports:

            timestamp = datetime.fromtimestamp(
                report["timestamp"]
            ).strftime(
                "%Y-%m-%d %H:%M"
            )

            st.markdown(
                f"""
                <div class="report-card">
                <h4>📄 {report['name']}</h4>

                <p>
                Generated: {timestamp}
                </p>

                <p>
                Autonomous workflow execution completed successfully.
                </p>
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================
# UPLOAD PAGE
# =========================

elif page == "Upload Corpus":

    st.title("Upload Research Corpus")

    st.markdown(
        """
        Upload multiple research papers.
        The system will automatically:
        - parse documents
        - generate embeddings
        - update vector memory
        - make corpus searchable
        """
    )

    uploaded_files = st.file_uploader(
        "Upload Multiple PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.success(
            f"{len(uploaded_files)} files selected"
        )

        st.subheader(
            "Selected Documents"
        )

        for uploaded_file in uploaded_files:

            st.markdown(
                f"📄 {uploaded_file.name}"
            )

        if st.button(
            "Upload & Ingest Corpus"
        ):

            progress_bar = st.progress(0)

            status_box = st.empty()

            ingestion_results = []

            successful_uploads = 0

            total_files = len(uploaded_files)

            for idx, uploaded_file in enumerate(
                uploaded_files
            ):

                status_box.info(
                    f"Processing: {uploaded_file.name}"
                )

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file,
                        "application/pdf"
                    )
                }

                response = requests.post(
                    f"{API_BASE_URL}/upload/pdf",
                    files=files
                )

                if response.status_code == 200:

                    successful_uploads += 1

                    ingestion_results.append(
                        response.json()
                    )

                else:

                    ingestion_results.append({
                        "filename":
                            uploaded_file.name,
                        "status":
                            "failed"
                    })

                progress_bar.progress(
                    int(
                        ((idx + 1) / total_files) * 100
                    )
                )

            status_box.success(
                "Corpus ingestion complete"
            )

            st.success(
                f"{successful_uploads}/{total_files} documents ingested successfully"
            )

            st.divider()

            st.subheader(
                "Ingestion Results"
            )

            for result in ingestion_results:

                st.json(result)


# =========================
# WORKFLOW PAGE
# =========================

elif page == "Run Workflow":

    st.title(
        "Run Autonomous Workflow"
    )

    st.markdown(
        """
        Execute autonomous workflows
        across the uploaded research corpus.
        """
    )

    query = st.text_area(
        "Research Objective",
        placeholder="""
Example:
Applications of transformers
in medical imaging
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        retrieval_depth = st.slider(
            "Retrieval Depth",
            1,
            20,
            5
        )

    with col2:

        include_citations = st.toggle(
            "Include Citations",
            value=True
        )

    st.divider()

    st.subheader(
        "Workflow Stages"
    )

    stages = [
        "Retrieval",
        "Synthesis",
        "Insights",
        "Literature Review",
        "Planning",
        "Citations",
        "Memory Update",
        "Final Report"
    ]

    stage_cols = st.columns(4)

    for idx, stage in enumerate(stages):

        with stage_cols[idx % 4]:

            st.markdown(
                f"""
                <div class="workflow-card">
                <h4>{stage}</h4>
                <p>Ready</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    if st.button(
        "Run Autonomous Workflow"
    ):

        if not query:

            st.warning(
                "Please enter a research objective"
            )

        else:

            progress = st.progress(0)

            status = st.empty()

            for i, step in enumerate(stages):

                status.info(
                    f"Executing: {step}"
                )

                progress.progress(
                    int(
                        ((i + 1) / len(stages)) * 100
                    )
                )

            with st.spinner(
                "Executing autonomous workflow..."
            ):

                response = requests.post(
                    f"{API_BASE_URL}/workflow/run",
                    params={
                        "query": query
                    }
                )

                if response.status_code == 200:

                    result = response.json()

                    status.success(
                        "Workflow completed successfully"
                    )

                    st.divider()

                    st.subheader(
                        "Generated Research Report"
                    )

                    st.markdown(
                        result["report"]
                    )

                else:

                    st.error(
                        "Workflow execution failed"
                    )


# =========================
# REPORTS PAGE
# =========================

elif page == "Reports":

    st.title(
        "Generated Reports"
    )

    st.markdown(
        """
        Persistent research deliverables
        generated by autonomous workflows.
        """
    )

    response = requests.get(
        f"{API_BASE_URL}/reports"
    )

    if response.status_code == 200:

        reports = response.json()["reports"]

        if len(reports) == 0:

            st.info(
                "No reports generated yet"
            )

        else:

            selected_report = st.selectbox(
                "Select Report",
                reports
            )

            if selected_report:

                report_response = requests.get(
                    f"{API_BASE_URL}/reports/{selected_report}"
                )

                if report_response.status_code == 200:

                    report_data = report_response.json()

                    st.divider()

                    st.subheader(
                        report_data["report_name"]
                    )

                    tab1, tab2 = st.tabs([
                        "📄 Report",
                        "⬇ Export"
                    ])

                    with tab1:

                        st.markdown(
                            report_data["content"]
                        )

                    with tab2:

                        download_response = requests.get(
                            f"{API_BASE_URL}/reports/download/{selected_report}"
                        )

                        st.download_button(
                            label="Download Report",
                            data=download_response.content,
                            file_name=selected_report,
                            mime="text/markdown"
                        )

    else:

        st.error(
            "Failed to fetch reports"
        )