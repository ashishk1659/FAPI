FROM python:3.10-slim

WORKDIR /test

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main /test/main

EXPOSE 8000

CMD ["uvicorn", "main.main:app", "--host", "0.0.0.0", "--port", "8000"]