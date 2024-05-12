FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt && apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* 

COPY ./app /app

EXPOSE 5000

CMD ["python", "main.py"]

HEALTHCHECK --interval=30s --timeout=30s --retries=3 CMD curl -f http://localhost:5000/status || exit 1