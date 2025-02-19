FROM python:3.12.1-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev \
    openssl

ADD requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /app/* /app/

