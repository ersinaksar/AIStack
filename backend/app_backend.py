# backend/app_backend.py
from fastapi import FastAPI, Request
from pydantic import BaseModel

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(request: ChatRequest):
    # Ollama LLM modeline bağlanma ve cevap alma işlemi yapılacak
    # Şimdilik sabit bir cevap döndürelim
    return {"reply": f"Echo: {request.message}"}

# Prometheus metriklerini expose etmek için
Instrumentator().instrument(app).expose(app)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)