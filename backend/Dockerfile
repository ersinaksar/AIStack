# backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi uvicorn

COPY . .

CMD ["uvicorn", "app_backend:app", "--host", "0.0.0.0", "--port", "8000"]