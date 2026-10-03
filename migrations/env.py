from alembic import context
from sqlalchemy import create_engine

from ctt.config import settings
from ctt.db import models  # noqa: F401
from ctt.db.base import Base

target_metadata = Base.metadata

with create_engine(settings.database_url).connect() as conn:
    context.configure(connection=conn, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()
