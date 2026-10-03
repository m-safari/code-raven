from fastapi import FastAPI

from ctt.api.routes import investigations

app = FastAPI(title="Codebase Time Traveler")
app.include_router(investigations.router)


@app.get("/health")
def health():
    return {"status": "ok"}
