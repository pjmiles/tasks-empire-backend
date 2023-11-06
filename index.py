from fastapi import FastAPI
from routes.users import user_router
from config.db import Base, engine

app = FastAPI(
    redoc_url="/api/v1/redoc",
    docs_url="/api/v1/docs",
)


@app.on_event("startup")
def start_up():
    Base.metadata.create_all(engine)


app.include_router(router=user_router)
