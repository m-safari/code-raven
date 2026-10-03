# Codebase Time Traveler (boilerplate)

Agentic investigation of behavioral regressions from Git history.
This skeleton only wires the infrastructure; the agent graph is a hello-world node.

## Run
    make up                       # postgres(pgvector) + redis + api + celery worker
    curl -X POST localhost:8000/investigations -H 'content-type: application/json' \
      -d '{"repo_url":"https://github.com/psf/requests","question":"When did X change?"}'
    docker compose exec postgres psql -U ctt -c "select id,status,report from investigations;"

Docs: http://localhost:8000/docs

## Layout
    src/ctt/api/       FastAPI app, routes, schemas
    src/ctt/agents/    LangGraph graphs (add tools/nodes here)
    src/ctt/workers/   Celery app and tasks
    src/ctt/db/        SQLAlchemy models/session
    src/ctt/llm/       Ollama/OpenRouter model factory (OpenAI-compatible)
    migrations/        Alembic (enables pgvector extension)
    tests/

## Next steps
Git/issue/test tools, hypothesis loop, pgvector embeddings table, Langfuse/MLflow, benchmark suite.
