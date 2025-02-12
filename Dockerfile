FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

WORKDIR /app

ENV PYTHONPATH=/app/investor_bulletin

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000




ENTRYPOINT ["sh", "./entrypoint.sh"]

CMD ["poetry", "run", "uvicorn", "investor_bulletin.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
