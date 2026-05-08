from agents.llm import generate_response


class PlanningAgent:

    def run(
        self,
        insights
    ):

        prompt = f"""
You are a research planning engine.

INSIGHTS:
{insights}

TASK:
Generate:

1. Research roadmap
2. Recommended next studies
3. High-priority experiments
4. Technical milestones
5. Dataset recommendations
6. Future implementation strategy
"""

        roadmap = generate_response(prompt)

        return {
            "roadmap": roadmap
        }