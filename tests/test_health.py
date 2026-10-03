from fastapi.testclient import TestClient

from ctt.agents.graph import build_graph
from ctt.api.main import app


def test_health():
    assert TestClient(app).get("/health").json() == {"status": "ok"}


def test_graph_hello():
    out = build_graph().invoke({"repo_url": "r", "question": "q"})
    assert "hello world" in out["report"]["summary"]
