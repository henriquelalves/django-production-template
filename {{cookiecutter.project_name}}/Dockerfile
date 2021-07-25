# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /djangoapp
COPY ./djangoapp/requirements.txt /djangoapp/requirements.txt
RUN pip install -r requirements.txt
COPY ./djangoapp /djangoapp
COPY ./config/wait-for-it.sh /djangoapp