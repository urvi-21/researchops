import os

from datetime import datetime

from reports.templates.research_template import (
    build_research_report
)

from memory.metadata_store import (
    MetadataStore
)


class ReportGenerator:

    def __init__(self):

        os.makedirs(
            "storage/reports",
            exist_ok=True
        )

        self.metadata_store = MetadataStore()

    def generate_report(
        self,
        state
    ):

        report = build_research_report(
            state
        )

        return report

    def save_report(
        self,
        report
    ):

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = (
            f"research_report_{timestamp}.md"
        )

        filepath = os.path.join(
            "storage/reports",
            filename
        )

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(report)

        self.metadata_store.add_report(
            report_name=filename,
            topic="research_workflow"
        )

        return filepath