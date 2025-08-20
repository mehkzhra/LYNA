from fastapi import FastAPI
from app.routers import chat

app = FastAPI()

@app.get("/")
def root():
    return {"message": "LYNA Backend is running 🚀"}

app.include_router(chat.router, prefix="/api", tags=["Chat"])
