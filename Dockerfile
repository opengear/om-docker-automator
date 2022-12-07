FROM python:3.11.0-alpine3.17

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt
