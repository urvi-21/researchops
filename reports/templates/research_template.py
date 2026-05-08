def build_research_report(state):

    return f"""
# RESEARCH REPORT

## QUERY

{state["query"]}

---

# EXECUTIVE SUMMARY

{state["synthesis"][:1500]}

---

# KEY INSIGHTS

{state["insights"]}

---

# LITERATURE REVIEW

{state["literature_review"]}

---

# FUTURE RESEARCH ROADMAP

{state["roadmap"]}

---

# CITATIONS

{state["citations"]}
"""