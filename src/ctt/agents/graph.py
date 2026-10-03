from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class InvestigationState(TypedDict, total=False):
    repo_url: str
    question: str
    report: dict


def hello(state: InvestigationState) -> dict:
    # Replace with planner / tool-calling / hypothesis nodes (use ctt.llm.get_llm()).
    summary = f"hello world: {state['question']} @ {state['repo_url']}"
    return {"report": {"summary": summary}}


def build_graph():
    g = StateGraph(InvestigationState)
    g.add_node("hello", hello)
    g.add_edge(START, "hello")
    g.add_edge("hello", END)
    return g.compile()
