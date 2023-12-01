FROM python:3.9-alpine3.13
LABEL maintainer="https://github.com/TatoSoselia"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-user