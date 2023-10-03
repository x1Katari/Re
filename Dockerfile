FROM python:3.11-slim-buster

WORKDIR /app

COPY pyproject.toml ./

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

COPY . .

WORKDIR /app/server