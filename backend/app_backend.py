# backend/app_backend.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def read_api():
    return {"message": "Hello from Backend!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)