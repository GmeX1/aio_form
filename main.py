from fastapi import FastAPI
from router import router_api
from database import SQLBase, engine

app = FastAPI(
    title='Register handle',
    description='Handle for registration form with telegram alerts'
)

SQLBase.metadata.create_all(bind=engine)
app.include_router(router_api)

