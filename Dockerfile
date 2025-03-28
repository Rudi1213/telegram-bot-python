FROM python:3.11.6-slim

WORKDIR /app
COPY . /app

RUN pip install psycopg2-binary
RUN pip install --upgrade poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["poetry", "run", "python", "main.py"]