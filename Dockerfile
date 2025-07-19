FROM python:3.11-slim-buster AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pytest

FROM python:3.11-slim-buster

WORKDIR /app

COPY --from=builder /usr/local/ /usr/local/
COPY app.py .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]