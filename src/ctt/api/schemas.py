import uuid

from pydantic import BaseModel, ConfigDict


class InvestigationCreate(BaseModel):
    repo_url: str
    question: str


class InvestigationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    repo_url: str
    question: str
    status: str
