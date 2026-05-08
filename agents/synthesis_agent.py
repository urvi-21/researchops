from agents.llm import generate_response


class SynthesisAgent:

    def build_context(
        self,
        retrieval_results
    ):

        contexts = []

        for result in retrieval_results:

            contexts.append(
                result["document"]["content"]
            )

        return "\n\n".join(contexts)

    def run(
        self,
        query,
        retrieval_results
    ):

        context = self.build_context(
            retrieval_results
        )

        prompt = f"""
You are a research synthesis engine.

TASK:
Generate a corpus-wide synthesis.

QUERY:
{query}

RETRIEVED CONTEXT:
{context}

OUTPUT:
Generate:
1. Core findings
2. Common patterns
3. Major themes
4. Technical observations
"""

        synthesis = generate_response(prompt)

        return {
            "query": query,
            "synthesis": synthesis
        }