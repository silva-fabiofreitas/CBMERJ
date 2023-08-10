FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN apt update
RUN pip install -qq -U install poetry

WORKDIR /app
RUN mkdir static_root
RUN mkdir media_root
COPY . .
RUN poetry install

CMD ["sh", "./entrypoint.sh"]