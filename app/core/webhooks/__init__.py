from core.webhooks import handlers
from fastapi import FastAPI

app = FastAPI(title="Код со смыслом Hackathon solution")
app.include_router(handlers.router, prefix="/api/v1")
