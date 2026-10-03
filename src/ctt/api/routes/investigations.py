from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ctt.api.schemas import InvestigationCreate, InvestigationOut
from ctt.db.models import Investigation
from ctt.db.session import get_db
from ctt.workers.tasks import run_investigation

router = APIRouter(prefix="/investigations", tags=["investigations"])


@router.post("", response_model=InvestigationOut, status_code=202)
def create_investigation(body: InvestigationCreate, db: Session = Depends(get_db)):
    inv = Investigation(repo_url=body.repo_url, question=body.question)
    db.add(inv)
    db.commit()
    run_investigation.delay(str(inv.id))
    return inv
