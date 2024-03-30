FROM python:3.9 AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install --no-cache-dir poetry && \
  poetry config virtualenvs.create false

RUN poetry install --no-root --no-interaction --no-ansi

FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

COPY src/ /app/src/

EXPOSE 5000

RUN useradd --no-create-home appuser
USER appuser

CMD ["gunicorn", "-w 4 -b 0.0.0.0:5000 src.app.main:app"]
