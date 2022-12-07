FROM python:3.11.0-alpine3.17

ADD . /scripts

WORKDIR /scripts

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt
