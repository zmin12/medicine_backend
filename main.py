from fastapi import FastAPI

from database import engine, Base
import models

from routers import medicine
from routers import user

from redis_client import redis_client

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    medicine.router
)

app.include_router(
    user.router,
    prefix="/user",
    tags=["user"]
)

@app.get("/")
def home():
    return {
        "msg":"backend running"
    }


@app.get("/redis-test")
def redis_test():

    if not redis_client:

        return {
            "status":"fallback"
        }

    return {
        "status":"success"
    }