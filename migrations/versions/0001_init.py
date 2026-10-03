"""init: pgvector extension + investigations

Revision ID: 0001
Revises:
"""
import sqlalchemy as sa
from alembic import op

revision = "0001"
down_revision = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")
    op.create_table(
        "investigations",
        sa.Column("id", sa.Uuid, primary_key=True),
        sa.Column("repo_url", sa.String, nullable=False),
        sa.Column("question", sa.String, nullable=False),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("investigations")
