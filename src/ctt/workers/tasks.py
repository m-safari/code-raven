import uuid

from ctt.agents.graph import build_graph
from ctt.db.models import Investigation
from ctt.db.mongo import reports
from ctt.db.session import SessionLocal
from ctt.workers.celery_app import celery_app


@celery_app.task(name="run_investigation")
def run_investigation(investigation_id: str) -> None:
    with SessionLocal() as db:
        inv = db.get(Investigation, uuid.UUID(investigation_id))
        inv.status = "running"
        db.commit()
        try:
            result = build_graph().invoke(
                {"repo_url": inv.repo_url, "question": inv.question}
            )
            doc, status = result["report"], "done"
        except Exception as exc:  # noqa: BLE001
            doc, status = {"error": str(exc)}, "failed"
        reports.replace_one(
            {"investigation_id": investigation_id},
            {"investigation_id": investigation_id, **doc},
            upsert=True,
        )
        inv.status = status
        db.commit()
