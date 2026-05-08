from agents.llm import generate_response


class InsightAgent:

    def run(
        self,
        synthesis
    ):

        prompt = f"""
You are a research insight generation engine.

SYNTHESIS:
{synthesis}

TASK:
Identify:

1. Research gaps
2. Emerging trends
3. Weaknesses in literature
4. Future opportunities
5. High-impact directions
"""

        insights = generate_response(prompt)

        return {
            "insights": insights
        }