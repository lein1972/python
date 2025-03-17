from fastapi import FastAPI
from my_api.routers import items

app = FastAPI()

app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "API is running"}