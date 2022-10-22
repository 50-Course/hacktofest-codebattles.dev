FROM python:3.10-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

COPY ./dev-requirements.txt /app

RUN --mount=type=cache,target=/root/.cache pip install -r dev-requirements.txt
