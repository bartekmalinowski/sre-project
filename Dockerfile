# Lekki obraz w python
FROM python:3.11-slim-buster AS builder

#enviroment config 
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pytest

FROM python:3.11-slim-buster

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
# Kopiujemy tylko kod aplikacji (bez folderu tests)
COPY app.py .
COPY requirements.txt .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]