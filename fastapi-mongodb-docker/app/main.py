import logging
import time

from fastapi import FastAPI
from pymongo.errors import PyMongoError

from app.database import client
from app.routers import items

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")

app = FastAPI(
    title="FastAPI + MongoDB Docker Demo",
    description="Simple FastAPI CRUD application using MongoDB and Docker.",
    version="1.0.0",
)


def check_mongodb_with_retry(max_retries: int = 15, delay_seconds: int = 3):
    for attempt in range(1, max_retries + 1):
        try:
            client.admin.command("ping")
            logger.info("MongoDB connection successful.")
            return
        except PyMongoError as exc:
            logger.warning(
                "MongoDB not ready (attempt %s/%s): %s",
                attempt, max_retries, exc
            )
            time.sleep(delay_seconds)

    raise RuntimeError("Could not connect to MongoDB after multiple retries.")


@app.on_event("startup")
def on_startup():
    check_mongodb_with_retry()


@app.get("/", tags=["health"])
def root():
    return {"status": "ok", "message": "FastAPI + MongoDB service is running"}


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "healthy"}


app.include_router(items.router)
