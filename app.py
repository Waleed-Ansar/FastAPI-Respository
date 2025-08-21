from fastapi import FastAPI
from code_base import router

app = FastAPI()
app.include_router(router)

# uvicorn app:app --reload