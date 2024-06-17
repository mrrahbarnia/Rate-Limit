FROM python:3.12.2-alpine3.19
LABEL maintainer="mrrahbarnia@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir app
WORKDIR /app

COPY ./requirements.txt /tmp/local.txt
COPY ./app /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/local.txt
RUN rm -rf /tmp
RUN adduser \
      --disabled-password \
      --no-create-home \
      mohammadreza && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R mohammadreza:mohammadreza /vol && \
    chmod -R 700 /vol
    # mkdir -p /logs && \
    # chmod -R a+rwx /logs

USER mohammadreza