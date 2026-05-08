from agents.llm import generate_response


class LiteratureReviewAgent:

    def run(
        self,
        query,
        synthesis
    ):

        prompt = f"""
You are an academic literature review engine.

QUERY:
{query}

SYNTHESIS:
{synthesis}

TASK:
Generate a structured literature review including:

1. Introduction
2. Existing methods
3. Major findings
4. Limitations
5. Research gaps
6. Conclusion
"""

        literature_review = generate_response(prompt)

        return {
            "literature_review": literature_review
        }