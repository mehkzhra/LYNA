from fastapi import FastAPI
from app.routers import cases, investigations, sessions, chat, solve, progress

app = FastAPI(
    title="Medical Case-Based Learning MVP",
    description="Educational simulation only — not medical advice.",
    version="0.1.0"
)

# Routers include
app.include_router(cases.router)
app.include_router(investigations.router)
app.include_router(sessions.router)
app.include_router(chat.router)
app.include_router(solve.router)
app.include_router(progress.router)

@app.get("/")
def home():
    return {"msg": "Welcome to Medical MVP Backend"}
