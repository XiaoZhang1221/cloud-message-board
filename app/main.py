from fastapi import FastAPI
from app.routers import message

app = FastAPI(title="Cloud Message Board")

app.include_router(message.router)

@app.get("/")
def root():
    return {"message": "cloud-message-board is running"}